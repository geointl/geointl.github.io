---
layout: page
title: Graph neural network simulators
description: AI-accelerated generalizable surrogate models for efficient physics simulations using graph neural networks.
importance: 1
category: work
related_publications: true
tags: physics-informed-machine-learning graph-neural-networks material-point-methods
images:
  slider: true
---

## Graph neural network simulators for granular flows

Accurate simulation of granular flow dynamics is essential for assessing geotechnical hazards such as landslides and debris flows. Granular flows involve dynamic particle rearrangement and exhibit complex solid–fluid-like behavior. Traditional numerical methods are often limited by computational cost at large scales or when repetitive analyses are required, while conventional machine learning surrogates typically do not capture the governing physics of granular flows. As a result, these surrogates are not generalizable or require prohibitively large amounts of training data.

We address these limitations with a graph neural network (GNN) simulator (GNS) {% cite choi2024graph %}. Graphs represent the state of dynamically evolving granular flows, and the GNN learns local interaction laws (e.g., energy and momentum exchange between grains) that govern the dynamics. Given the current flow state, GNS predicts the next state through Euler explicit integration. We implement a multi-GPU PyTorch framework based on distributed data parallelism (DDP) that supports different material types. 

> The open-source code and data are available on [GitHub](https://github.com/geoelements/gns).

### Demonstration

We train GNS on a limited set of granular flow trajectories and evaluate it on granular column collapse. GNS accurately predicts flow dynamics for column collapses with different aspect ratios and friction angles not seen during training. 

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-column-short-21.gif" title="GNS vs MPM: short column, 21° friction" class="img-fluid rounded" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-column-tall-42.gif" title="GNS vs MPM: tall column, 42° friction" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    GNS prediction compared to MPM for the collapse of short granular column with friction angle of 21° (left) and tall granular column with friction angle of 42° (right).
</div>

The model is trained on granular masses with an aspect ratio of 1.0 but generalizes to configurations with markedly different flow behavior.

<div class="row mt-3 justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-aspect-ratio-generalization.png" title="Generalizability across aspect ratios" class="img-fluid rounded" sizes="(min-width: 576px) 66vw, 95vw" %}
    </div>
</div>
<div class="caption">
    Generalizability of GNS: the model is trained on the granular mass with aspect ratio of 1.0, but can be generalized to various aspect ratios not seen during training, which have different flow dynamics.
</div>

GNS also captures granular flow interaction with barriers. Training data include cube-shaped granular masses interacting with one or two barriers. We demonstrate generalization by upscaling geometry size and testing unseen barrier configurations—the GNS reproduces ground-truth behavior from high-fidelity material point method (MPM) simulations.


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/gns-baffle.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=false loop=true muted=true %}
    </div>
</div>
<div class="caption">
    Graph neural network-based simulator (GNS) prediction on granular flow interacting with barriers (GNS vs MPM). Original demo: [YouTube](https://www.youtube.com/watch?v=VL74gzi--OQ).
</div>

### Computational efficiency

We compare rollout time per timestep between MPM and GNS for varying numbers of material points. For the 2D column-collapse model and the 3D barrier-flow model, GNS achieves up to a few thousand times speedup over high-fidelity MPM simulation while maintaining predictive accuracy on held-out configurations.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-computation-time.png" title="MPM vs GNS computation time" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Computation time of MPM and GNS rollout per timestep for varying number of material points. The 2D model is the one used for simulating granular column collapse, and the 3D model is for the flow with barriers.
</div>

### Case history validation

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/lsfd.mp4" class="img-fluid rounded" controls=true autoplay=false loop=true muted=true %}
    </div>
</div>
<div class="caption">
    GNS simulation of a Lower San Fernando Dam (1971) {% cite choi2026differentiablerunout %}.
</div>

## Broader applications

Beyond granular flows, GNN-based approaches extend to fluid flow and solid mechanics problems.

<swiper-container keyboard="true" navigation="true" pagination="true" pagination-clickable="true" pagination-dynamic-bullets="true" rewind="true">
  <swiper-slide>
    <div class="row justify-content-sm-center">
      <div class="col-sm-8">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-cylinder.gif" title="GNS: cylinder flow" class="img-fluid rounded" %}
      </div>
    </div>
    <div class="caption">
      Cylinder flow with GNS {% cite kumar2023accelerating %}. GNS is orders of magnitude faster than conventioanl CFD 
    </div>
  </swiper-slide>
  <swiper-slide>
    <div class="row justify-content-sm-center">
      <div class="col-sm-10">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-fem-fracture.png" title="Hybrid GNN-FEM crack propagation" class="img-fluid rounded" %}
      </div>
    </div>
    <div class="caption">
      A Hybrid GNN–FEM Framework for Phase-Field Fracture Simulation: full FEM (top) compared with hybrid GNN-FEM with physics-informed domain decomposition (bottom) {% cite moon2026hybrid %}.
    </div>
  </swiper-slide>
  <swiper-slide>
    <div class="row justify-content-sm-center">
      <div class="col-sm-4">
        {% include figure.liquid loading="eager" path="assets/img/gns-column/gns-porous.gif" title="GNS: porous media flow" class="img-fluid rounded" max-width="280px" %}
      </div>
    </div>
    <div class="caption">
      Flow through porous media simulated with GNS (ongoing work).
    </div>
  </swiper-slide>
</swiper-container>

