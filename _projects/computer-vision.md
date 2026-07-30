---
layout: page
title: Computer vision for infrastructure inspection and hazard detection
description: Deep learning-based computer vision for automated defect detection and hazard assessment in civil infrastructure.
importance: 1
category: work
related_publications: true
tags: hazard-detection computer-vision object-detection instance-segmentation
---

Computer vision is transforming infrastructure inspection by enabling automated detection and localization of structural defects from images and sensing data. We develop deep learning-based computer vision models for infrastructure health monitoring and hazard detection, with an emphasis on robust object detection and instance segmentation for civil engineering applications. By automating labor-intensive and error-prone inspection tasks, these methods provide faster, more consistent, and scalable assessments of infrastructure conditions. Our current research includes automated concrete crack detection from visual images and tunnel lining segmentation from ground-penetrating radar (GPR) images.


<div class="row mt-3 justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/crack-cnn.png" title="Automated concrete crack detection" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Automated concrete crack detection using deep learning-based instance segmentation models (Mask R-CNN (two-stage model) and YOLO (single-stage model)) {% cite choi2024application %}.
</div>

<div class="row mt-3 justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/gpr-cnn.png" title="Automated tunnel lining segmentation from GPR images" class="img-fluid rounded" %}
    </div>
</div>
<div class="caption">
    Automated tunnel lining segmentation from ground-penetrating radar (GPR) images using deep learning-based object detection and segmentation (Mask R-CNN (two-stage model) and YOLO (single-stage model)) {% cite bae2025tunnel %}.
</div>