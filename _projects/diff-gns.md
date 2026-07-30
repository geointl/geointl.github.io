---
layout: page
title: Inverse analysis for granular flows using differentiable graph network simulator
description: Gradient-based inverse analysis and inverse design with GNS + automatic differentiation (AD).
importance: 1
category: work
related_publications: true
tags: differentiable-programming inverse-modeling design-optimization model-discovery graph-neural-networks
---

Inverse analysis provides a systematic way to infer unknown parameters or optimize designs based on observed or desired granular flow behavior. Typical applications include estimating material properties and initial conditions, as well as designing earth structures for flow mitigation.

Existing approaches have several limitations. High-fidelity numerical simulators such as DEM and MPM are computationally expensive because inverse analysis requires repeated forward simulations, while their non-differentiable formulations prevent the use of efficient gradient-based optimization. Conventional surrogate models based on machine learning or statistical methods often generalize poorly beyond their training domain because they do not explicitly capture the underlying flow physics or are restricted to low-dimensional parameter spaces.

To address these challenges, we develop a differentiable graph neural network simulator (Diff-GNS) for inverse analysis of granular flows {% cite choi2024inverse %}. By combining the computational efficiency and physics-aware representation of graph neural network simulators with automatic differentiation, the proposed framework enables efficient gradient-based optimization for estimating unknown parameters and solving inverse design problems.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-framework.png" title="Gradient-based optimization for inverse problems in granular flows" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Diff-GNS solves inverse problems in granular flows efficiently. (a) Graph neural network-based simulators (GNS) provide an efficient and generalizable surrogate for high-fidelity numerical simulators. (b) By leveraging the differentiability of GNS and automatic differentiation, gradient-based optimization is used to solve inverse problems involving a high dimensional parameter set.
</div>

> Open-source code and data are available on [GitHub](https://github.com/geoelements/gns-inverse-examples).

## Demonstration

Inverse problems involve determining the underlying causes or parameters from observed effects or outcomes. We demonstrate the effectiveness of our methodology across three distinct inverse analysis scenarios: (1) inferring material parameters from runout, (2) Inferring initial physical states of granular mass from post-failure deposit, and (3) optimizing geostructure design to control runouts.

### (1) Inferring material parameters from runout

The objective of the inverse analysis in this section is to infer the friction angle of the granular column mass that produces a target runout distance from the friction angle of 21 degrees.

The following figure shows the optimization progress of the proposed framework. It identifies the correct friction angle (=22.45°) close to the target value (=21°) as well as the overall geometry of the final deposit. The computation time for the optimization accomplishes about 126× speed-up compared to solely relying on the high-fidelity numerical simulator owing to the computation efficiency of the Diff-GNS framework.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-friction-opt.png" title="Optimization history for friction angle inverse analysis" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Optimization history. As iteration progresses, the proposed method identifies the friction angle (=22.45°) close to the target value (=21°) as well as the geometry of the final deposit.
</div>

### (2) Inferring initial physical states of granular mass from post-failure deposit

The proposed framework is particularly effective for high-dimensional inverse problems because it leverages reverse-mode automatic differentiation. In this example, we consider a multi-layered granular column, where each layer has a different initial velocity (left figure).

The objective is to estimate the initial velocity of each layer using only the observed post-failure deposit. As the optimization progresses, the estimated velocity profile gradually converges to the ground truth (black line), as shown in the figure on the right.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-velocity-opt.png" title="Optimization of initial velocity profile" class="img-fluid rounded" %}
    </div>
</div>

The animations below compare the ground-truth and estimated granular flows from the optimized initial velocity. The runout closely matches the ground-truth behavior.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-ground-truth.gif" title="Ground truth rollout" class="img-fluid rounded" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-estimated.gif" title="Result from inverse estimation" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Ground truth (left) and result from inverse estimation (right).
</div>

### (3) Design optimization of geostructures

The proposed framework can also be applied to the inverse design of earth structures, where design parameters are optimized to achieve a desired flow outcome. Here, we consider the design optimization of a debris-resisting baffle dam array.

The figure below illustrates the optimization process for determining the baffle locations that guide the centroid of the flow toe to a target location. As the optimization progresses, the design gradually converges to the optimal configuration.

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gns-inverse/gns-inverse-baffle-opt.png" title="Baffle design optimization history" class="img-fluid rounded" %}
    </div>
</div>

<div class="row mt-3">
    <div class="col-12 mt-3 mt-md-0">
        {% include video.liquid path="https://www.youtube.com/embed/h1Zf33CacTU" class="w-100 rounded z-depth-1" width="100%" height="540" %}
    </div>
</div>
<div class="caption">
    Demonstration video. Original: [YouTube](https://www.youtube.com/watch?v=h1Zf33CacTU).
</div>


## Practical applications to geohazard analysis

Beyond the novel methodological contribution, we advance the Diff-GNS for case history back-analysis, which proves the practical value of the framework. See our publications for more details {% cite choi2026differentiablerunout choi2026differentiable %}.

