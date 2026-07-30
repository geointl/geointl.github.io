---
layout: about
title: home
permalink: /
subtitle: <a href='https://www.umass.edu/engineering/civil-and-environmental-engineering'>Civil and Environmental Engineering</a>, UMass Amherst

selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # icons rendered below intro (same set as Team/PI) to avoid duplicating after news

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

# latest_posts:
#   enabled: true
#   scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
#   limit: 3 # leave blank to include all the blog posts
---

<style>
  @media (min-width: 576px) {
    .post .profile {
      width: 20%;
      max-width: 200px;
    }
  }

  .home-social {
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    text-align: left;
  }

  .home-social .contact-icons {
    font-size: 1.4rem;
  }

  .home-social .contact-icons a {
    margin-right: 0.7rem;
    color: var(--global-text-color, #333);
  }

  .home-social .contact-icons a:hover {
    color: var(--global-theme-color, #4285f4);
  }

  /* CV stays on Team/PI; hide only on home */
  .home-social .contact-icons a[title="Cv pdf"] {
    display: none;
  }
</style>

Welcome to GeoIntelligence research group at UMass Amherst. We aim to advance the frontier of geotechnical engineering through AI-enhanced computational methods. Our research focuses on AI-enhanced physics simulation, differentiable inverse modeling, and agentic AI to enable geotechnical analyses beyond the capabilities of conventional approaches.

<div class="home-social">
  <div class="contact-icons">{% social_links %}</div>
</div>
