---
layout: page
title: Operator learning for physics-informed surrogate for geotechnical analysis
description: 
importance: 1
category: work
related_publications: true
tags: physics-informed-machine-learning neural-operators finite-element-methods
---

> {% cite choi2026operator %}

Deep Operator Networks (DeepONets) have emerged as a powerful surrogate modeling framework for learning solution operators in PDE-governed systems. While their use is expanding across engineering disciplines, applications in geotechnical engineering remain limited. This study systematically evaluates several DeepONet architectures for the consolidation problem. We initially consider three architectures: a standard DeepONet with the coefficient of consolidation embedded in the branch net (Models 1 and 2), and a physics-inspired architecture with the coefficient embedded in the trunk net (Model 3). Results show that Model 3 outperforms the standard configurations (Models 1 and 2) but still has limitations when the target solution (excess pore pressures) exhibits significant variation. To overcome this limitation, we propose a Trunknet Fourier feature-enhanced DeepONet (Model 4) that addresses the identified limitations by capturing rapidly varying functions. We further extend Model 4 to 3D scenarios. Although the computational speedup can be modest in the 1D case (1.5-100x compared with traditional solvers), the speedup becomes more pronounced in 3D, reaching approximately 1000x. 


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/deeponet-consol.png" title="DeepONet for consolidation" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Operators enable real-time prediction for complex geomechanical process which opens up new possibilities for large scale uncertainty quantification and optimization tasks where conventional numerical method alone is hard to handle. The above example shows a real-time prediction for 3D consolidation process from our enhanced DeepONet compared to high fidelity numerical solution.  
</div>


Leveraging this efficiency, we offer a conceptual demonstration of DeepONet’s potential to accelerate uncertainty quantification in a 3D consolidation problem. 

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/deeponet-consol-uq.png" title="DeepONet for uncertainty qunatification in consolidation" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    DeepONet quantifies uncertainties in the degree of consolidation $U(t)$ across a 3D domain almost instantaneously, enabling rapid assessments that would be computationally intensive using traditional methods.
</div>

Overall, the study highlights the potential of DeepONets to enable efficient, generalizable surrogate modeling in geotechnical applications, advancing the integration of scientific machine learning in geotechnics, which is at an early stage.