# CV (LaTeX)

Build: `cd cv && latexmk` → `assets/pdf/CV_ChoiYJ.pdf` (LuaLaTeX + biber).
The deploy workflow runs the same command, so the website always serves the current PDF.

## Where things go

| What                                                        | File                                                        |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| Look (fonts, colors, spacing, entry layout)                 | `cvstyle.sty` only                                          |
| Header, section order, hide/show a section                  | `cv.tex` (one `\input` line per section)                    |
| Section content                                             | `sections/*.tex` (each file starts with a template comment) |
| Published papers and public preprints (also on the website) | `../_bibliography/papers.bib`                               |
| Manuscripts under review that are not public yet            | `manuscripts.bib`                                           |
| Conference talks without a proceedings paper                | `presentations.bib`                                         |

Placeholders `sections/mentoring.tex` and `sections/funding.tex` are commented out in `cv.tex`;
uncomment the line once they have entries.

## How a paper is sorted into a list

| List                                      | Rule                                                             |
| ----------------------------------------- | ---------------------------------------------------------------- |
| Peer-Reviewed Journal Articles            | `@article`, no `pubstate` (or `inpress`)                         |
| Manuscripts Under Review                  | `pubstate = {submitted}`, or any entry in `manuscripts.bib`      |
| Conference Papers                         | `@inproceedings` / `@incollection`                               |
| Peer-Reviewed Korean Journal Articles     | `keywords = {korean}`                                            |
| Conference Presentations                  | any entry in `presentations.bib`                                 |
| (not listed)                              | `pubstate = {prepublished}`: a preprint you don't want in the CV |

Numbers count up from the oldest paper, so existing numbers never change.
An entry that matches no list is reported as a warning in `build/CV_ChoiYJ.log`.

## Extra fields

```bibtex
author+an   = {2=equal; 3=corresponding}   % † and *; also: presenter, advisee (underlined)
code        = {https://github.com/...}     % "Code" link (the website shows a Code button too)
pubstate    = {submitted}                  % under review
submittedto = {Computers and Geotechnics}  % shown as "Under review in ..."
keywords    = {korean}
```

Your own name is bolded automatically (`\cvselfname{Choi}{Yongjin}` in `cv.tex`).
DOI, arXiv, and Code links are printed as clickable words after each entry.

## Automatic updates

- `.github/workflows/check-new-publications.yml` (weekly) looks for new papers on ORCID, OpenAlex,
  and the Google Scholar titles in `_data/citations.yml`, and opens a pull request that adds them
  to `papers.bib`. Review the checklist in the PR, then merge. Papers that aren't yours go in
  `_bibliography/ignore.yml`.
- Merging rebuilds the website, which rebuilds this PDF.
