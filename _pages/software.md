---
layout: page
permalink: /software/
title: Software
# description: Open-source software for geomechanics simulation and machine learning.
nav: true
nav_order: 4
---

## cbgeopy

`cbgeopy` is a tool to generate material point method (MPM) model. It supports making multi-layered material points for mountain-like topography in 2D and 3D and `vtk` or `html` type visualization. The output model and associated files can be directly used as input files for CB-geo MPM.

[<i class="fa-solid fa-book fa-sm"></i> Documentation](https://cbgeopy.readthedocs.io){:target="_blank"} &nbsp;·&nbsp; [<i class="fa-brands fa-github fa-sm"></i> GitHub](https://github.com/yjchoi1/cbgeopy){:target="_blank"}

## Graph Network Simulator (GNS) and MeshNet

We participate in open-source Pytorch-based GNS and MeshNet project that support training on multiple nodes with multiple GPUs. GNS is a generalizable, efficient, and accurate machine learning-based surrogate simulator for particulate and fluid systems using Graph Neural Networks. GNS code is a viable surrogate for numerical methods such as Material Point Method, Smooth Particle Hydrodynamics and Computational Fluid dynamics. GNS exploits distributed data parallelism to achieve fast multi-GPU training. The GNS code can handle complex boundary conditions and multi-material interactions. MeshNet is a scalable surrogate simulator for any mesh-based models like Finite Element Analysis, Computational Fluid Dynammics, and Finite Difference Methods.

[<i class="fa-brands fa-github fa-sm"></i> GitHub](https://github.com/geoelements/gns){:target="_blank"}
