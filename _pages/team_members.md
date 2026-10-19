---
layout: profiles
permalink: /team/members/
title: Members
nav: false

undergrads:
  - name: Tomer Elkayam
    image: tomer_elkayam.jpg
    start: 2026
    email: telkayam@umass.edu
---

Are you interested in joining our team? See our [Openings]({{ '/openings/' | relative_url }}) page.

{% comment %}
Placeholder member entries — copy into the front matter above when people join.
Photos go in assets/img/members/ (any portrait headshot; cropped to 4:5 automatically).
Only `name` is required; cards render in front-matter order, 4 per row.
Contact fields (email, url, github_username, linkedin_username) show as icon links.
When someone leaves, add `end:` and move their entry to `alumni:`.

postdocs:
  - name: Jane Smith
    # image: jane.jpg         # filename in assets/img/members/
    start: 2024
    topics: Scientific machine learning, inverse analysis
    email: jane@umass.edu     # optional
    url: https://example.com  # optional personal webpage
    github_username: janesmith    # optional
    linkedin_username: janesmith  # optional

phd_students:
  - name: Bob Lee
    # image: bob.jpg
    start: 2023
    topics: Uncertainty quantification, HPC geotechnics

ms_students:
  - name: Alice Kim
    # image: alice.jpg
    start: 2025
    topics: AI-aided hazard detection

undergrads:
  - name: Tom Park
    # image: tom.jpg
    start: 2025
    topics: Data analysis

alumni:
  - name: Sam Lee
    # image: sam.jpg
    start: 2022
    end: 2026                 # shown as "2022–2026"
    topics: MS 2026, now at Example Corp
{% endcomment %}
