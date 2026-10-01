#!/usr/bin/env python3
"""Find publications that are missing from _bibliography/papers.bib.

Sources (no API keys needed):
  * ORCID public record   -- orcid_id in _data/socials.yml
  * OpenAlex works        -- matched by the same ORCID (wider, but may include
                             papers by other people with the same name)
  * Google Scholar titles -- cached in _data/citations.yml by
                             bin/update_scholar_citations.py (titles only)

New DOIs are turned into BibTeX entries from doi.org metadata and, with
--write, added to the top of papers.bib. Titles without a DOI are only listed
in the report. The weekly workflow opens a pull request with the result, so
nothing reaches the website or the CV without review.

DOIs or titles that should never be proposed go in _bibliography/ignore.yml.

Usage: python bin/check_new_publications.py [--write] [--report PATH]
"""

import argparse
import difflib
import html
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request

import yaml

PAPERS_BIB = "_bibliography/papers.bib"
MANUSCRIPTS_BIB = "cv/manuscripts.bib"
IGNORE_FILE = "_bibliography/ignore.yml"
SOCIALS_FILE = "_data/socials.yml"
CITATIONS_FILE = "_data/citations.yml"
CONFIG_FILE = "_config.yml"

USER_AGENT = "al-folio-publication-check (https://github.com/alshedivat/al-folio)"
PREPRINT_DOI_PREFIXES = ("10.48550/", "10.2139/", "10.31224/", "10.21203/", "10.20944/", "10.1101/")
TITLE_MATCH = 0.9
STOPWORDS = {"a", "an", "the", "on", "of", "for", "in", "and", "to", "with", "using", "via", "toward", "towards"}


# --------------------------------------------------------------------------- helpers
def http_json(url, accept="application/json"):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def norm_doi(doi):
    doi = (doi or "").strip().lower()
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", doi)


def norm_title(title):
    title = unicodedata.normalize("NFKD", html.unescape(title or ""))
    return re.sub(r"[^a-z0-9]", "", title.lower())


def clean_title(title):
    title = re.sub(r"<[^>]+>", "", html.unescape(title or ""))  # Crossref titles may contain <i>, <sub>
    return re.sub(r"\s+", " ", title).strip()


def is_preprint(doi, kind=""):
    return doi.startswith(PREPRINT_DOI_PREFIXES) or kind in {"preprint", "posted-content"}


def load_yaml(path):
    try:
        with open(path) as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}


# --------------------------------------------------------------------------- known entries
def read_bib_entries(path):
    """Return [{key, title, doi, pubstate}] using a light regex parse."""
    try:
        text = open(path).read()
    except FileNotFoundError:
        return []
    entries = []
    for chunk in re.split(r"(?m)^(?=@)", text):
        m = re.match(r"@\w+\{([^,\s]+),", chunk)
        if not m:
            continue

        def field(name):
            f = re.search(r"(?mi)^\s*" + re.escape(name) + r"\s*=\s*\{(.*)\},?\s*$", chunk)
            return f.group(1).strip() if f else ""

        entries.append(
            {"key": m.group(1), "title": field("title"), "doi": norm_doi(field("doi")), "pubstate": field("pubstate"), "file": path}
        )
    return entries


def match_title(title, entries):
    target = norm_title(title)
    if not target:
        return None
    best, best_ratio = None, 0.0
    for e in entries:
        ratio = difflib.SequenceMatcher(None, target, norm_title(e["title"])).ratio()
        if ratio > best_ratio:
            best, best_ratio = e, ratio
    return best if best_ratio >= TITLE_MATCH else None


# --------------------------------------------------------------------------- sources
def from_orcid(orcid):
    data = http_json(f"https://pub.orcid.org/v3.0/{orcid}/works")
    works = []
    for group in data.get("group", []):
        summary = group["work-summary"][0]
        ids = {i["external-id-type"]: i["external-id-value"] for i in summary.get("external-ids", {}).get("external-id", [])}
        year = ((summary.get("publication-date") or {}).get("year") or {}).get("value", "")
        works.append({"doi": norm_doi(ids.get("doi")), "title": summary["title"]["title"]["value"], "year": year, "type": summary.get("type", ""), "source": "ORCID"})
    return works


def from_openalex(orcid):
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f"author.orcid:{orcid}", "per-page": 200, "select": "doi,title,publication_year,type"})
    data = http_json(url)
    return [
        {"doi": norm_doi(w.get("doi")), "title": w.get("title") or "", "year": str(w.get("publication_year") or ""), "type": w.get("type", ""), "source": "OpenAlex"}
        for w in data.get("results", [])
    ]


def from_scholar_cache():
    papers = (load_yaml(CITATIONS_FILE).get("papers") or {}).values()
    return [{"doi": "", "title": p.get("title", ""), "year": str(p.get("year", "")), "type": "", "source": "Google Scholar"} for p in papers]


# --------------------------------------------------------------------------- BibTeX
def bib_entry(doi, existing_keys, self_family, self_given):
    """Build a BibTeX entry from doi.org CSL-JSON (works for Crossref and DataCite DOIs)."""
    csl = http_json(f"https://doi.org/{urllib.parse.quote(doi)}", accept="application/vnd.citationstyles.csl+json")
    kind = csl.get("type", "")
    preprint = is_preprint(doi, kind) or kind in {"article", "report"}
    entry_type = {"article-journal": "article", "paper-conference": "inproceedings", "chapter": "incollection"}.get(kind, "article")

    authors = []
    for a in csl.get("author", []):
        family, given = a.get("family", "").strip(), a.get("given", "").strip()
        if family.lower() == self_family.lower() and re.sub(r"[\s-]", "", given).lower() == self_given.lower():
            given = self_given  # e.g. "Yong-Jin" -> "Yongjin"
        authors.append(f"{family}, {given}" if given else family or a.get("literal", ""))

    parts = (csl.get("published-print") or csl.get("published-online") or csl.get("issued") or {}).get("date-parts") or [[""]]
    year = str(parts[0][0] or "")
    title = clean_title(csl.get("title", ""))
    container = csl.get("container-title", "")
    if isinstance(container, list):
        container = container[0] if container else ""
    container = clean_title(container)

    first = re.sub(r"[^a-z]", "", unicodedata.normalize("NFKD", (csl.get("author") or [{}])[0].get("family", "anon")).lower())
    word = next((w for w in re.findall(r"[a-z]+", title.lower()) if w not in STOPWORDS), "paper")
    key, n = f"{first}{year}{word}", 1
    while key in existing_keys:
        n += 1
        key = f"{first}{year}{word}{n}"
    existing_keys.add(key)

    fields = [("title", title), ("author", " and ".join(authors))]
    fields.append(("booktitle" if entry_type in {"inproceedings", "incollection"} else "journal", container or ("Preprint" if preprint else "")))
    fields += [
        ("volume", str(csl.get("volume", ""))),
        ("number", str(csl.get("issue", ""))),
        ("pages", str(csl.get("page", "")).replace("-", "--")),
        ("year", year),
        ("publisher", csl.get("publisher", "")),
        ("doi", doi),
    ]
    if preprint:
        fields.append(("pubstate", "prepublished"))  # on the website, not in the CV until you decide
    fields = [(k, v) for k, v in fields if v]
    width = max(len(k) for k, _ in fields)
    body = ",\n".join(f"  {k.ljust(width)} = {{{v}}}" for k, v in fields)
    return key, f"@{entry_type}{{{key},\n{body}\n}}\n", {"title": title, "venue": container, "year": year, "preprint": preprint}


# --------------------------------------------------------------------------- main
def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="add new entries to papers.bib")
    parser.add_argument("--report", default="new_publications.md", help="markdown report path")
    args = parser.parse_args()

    orcid = str(load_yaml(SOCIALS_FILE).get("orcid_id") or "").strip()
    scholar = load_yaml(CONFIG_FILE).get("scholar") or {}
    self_family = (scholar.get("last_name") or [""])[0]
    self_given = (scholar.get("first_name") or [""])[0]
    ignore = load_yaml(IGNORE_FILE)
    ignored_dois = {norm_doi(d) for d in ignore.get("dois") or []}
    ignored_titles = [{"title": t} for t in ignore.get("titles") or []]

    papers = read_bib_entries(PAPERS_BIB)
    manuscripts = read_bib_entries(MANUSCRIPTS_BIB)
    known = papers + manuscripts
    known_dois = {e["doi"] for e in known if e["doi"]}
    existing_keys = {e["key"] for e in known}

    works, errors = [], []
    for name, fetch in [("ORCID", lambda: from_orcid(orcid) if orcid else []), ("OpenAlex", lambda: from_openalex(orcid) if orcid else []), ("Google Scholar cache", from_scholar_cache)]:
        try:
            works += fetch()
        except Exception as exc:  # one source failing should not stop the others
            errors.append(f"{name}: {exc}")
    if not orcid:
        errors.append("No orcid_id in _data/socials.yml; ORCID and OpenAlex were skipped.")

    candidates, seen = [], set()
    for w in works:
        doi, title = w["doi"], w["title"]
        tag = doi or norm_title(title)
        if not tag or tag in seen:
            continue
        seen.add(tag)
        if doi in ignored_dois or match_title(title, ignored_titles) or (doi and doi in known_dois):
            continue
        match = match_title(title, known)
        if match:
            match_is_final = match["file"] == PAPERS_BIB and match["pubstate"] not in {"submitted", "prepublished"}
            if match_is_final or is_preprint(doi, w["type"]) or not doi:
                continue  # already listed (or just another version of it)
        sources = sorted({x["source"] for x in works if (doi and x["doi"] == doi) or norm_title(x["title"]) == norm_title(title)})
        candidates.append({**w, "sources": ", ".join(sources), "replaces": match["key"] if match else ""})

    added, no_doi = [], []
    for c in candidates:
        if not c["doi"]:
            no_doi.append(c)
            continue
        try:
            key, entry, meta = bib_entry(c["doi"], existing_keys, self_family, self_given)
            added.append({**c, **meta, "key": key, "entry": entry})
        except Exception as exc:
            errors.append(f"{c['doi']}: could not fetch metadata ({exc})")
            no_doi.append(c)

    if args.write and added:
        text = open(PAPERS_BIB).read()
        open(PAPERS_BIB, "w").write("".join(a["entry"] + "\n" for a in added) + text)

    lines = ["## New publications found", ""]
    if added:
        lines += ["Added to the top of `_bibliography/papers.bib`:", "", "| Key | Title | Venue | Year | Found in |", "|---|---|---|---|---|"]
        for a in added:
            note = f" (newer version of `{a['replaces']}`; delete that entry)" if a["replaces"] else ""
            note += " — preprint, hidden from the CV" if a["preprint"] else ""
            lines.append(f"| `{a['key']}` | {a['title']}{note} | {a['venue']} | {a['year']} | {a['sources']} |")
        lines += [
            "",
            "### Before merging",
            "- [ ] Not your paper? Delete the entry and add its DOI to `_bibliography/ignore.yml`.",
            "- [ ] Korean journal? Add `keywords = {korean}`.",
            "- [ ] Equal-contribution / corresponding authors: `author+an = {2=equal; 3=corresponding}`.",
            "- [ ] Code repository: `code = {https://github.com/...}`.",
            "- [ ] Preprint under review? Change `pubstate` to `submitted` and add `submittedto = {Journal}`.",
            "- [ ] Published version of a paper in `cv/manuscripts.bib`? Delete it there.",
            "",
        ]
    else:
        lines += ["No new DOIs found.", ""]
    if no_doi:
        lines += ["### Found without a DOI (add manually if they are yours)", ""]
        lines += [f"- {c['title']} ({c['year']}) — {c['sources']}" for c in no_doi]
        lines.append("")
    if errors:
        lines += ["### Problems during the check", ""] + [f"- {e}" for e in errors] + [""]
    open(args.report, "w").write("\n".join(lines))

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
