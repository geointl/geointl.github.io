---
title: Onboarding
nav_order: 1
description: Tools, software, and learning materials for new lab members.
---

# Welcome & Onboarding Overview

Welcome to the lab\! A PhD or research journey is like a marathon—building a solid foundation early on will help you move faster, go further, and work efficiently. Below are helpful tools, software, and learning materials to help you get started. You don’t need to build the knowledge at once, or every item. Begin step-by-step, starting with what you need, depending on the stage of your academic career.&nbsp;

---

# Prerequisites & Essential Tools

### Linux & Unix Shell

Our group pursues open-source development and the ecosystem. Most ML/AI tools and open-source software are developed in Linux environments. Learn basic Linux and shell skills for both local and HPC workflows.

* **Unix Tutorial:** [Linux/Unix Tutorial](https://info-ee.surrey.ac.uk/Teaching/Unix/)  
* **Shell Basics:** [Unix Shell Novice Guide](https://swcarpentry.github.io/shell-novice/06-script.html)

### Python & Virtual Environments

Python is our primary programming language for research, scientific computing, and numerical methods. Always manage dependencies using isolated virtual environments.

* **Numerical Python Guide:** [Python Programming & Numerical Methods](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html)  
* **Virtual Environments:** [Python venv Tutorial](https://docs.python.org/3/tutorial/venv.html)

### Code IDE

We primarily use Visual Studio Code (VS Code) for local development and remote server connections.

* **VS Code:** [Download & Setup](https://code.visualstudio.com/)

### Version Control & Collaboration (Git & GitHub)

Manual tracking of code changes gets messy quickly. We use Git for version control and GitHub for code repository and team collaboration. The standard way of code sharing with your collaborators and team is through GitHub rather than email or messengers, whether it is during development or in the deployment stage.&nbsp;

* **Git Interactive Learning:** [Learn Git Branching](https://learngitbranching.js.org/)  
* **Git & GitHub Guide:** [Git & GitHub for Engineers](https://yjchoi1.github.io/devops-basics-engineers/02-git/git/)

### High-Performance Computing (Unity HPC)

Start developing prototypes on local machines, then scale up computationally demanding tasks on the Unity HPC platform.

* **Account Setup:** Sign up at [Unity HPC](https://unityhpc.org/). Contact yongjin if group credentials are required during signup – our group has unlimited usage.&nbsp;  
* **Getting Started:** [Unity Documentation](https://unityhpc.org/documentation/get-started/)

### AI Development Agents

We strongly encourage using AI coding agents to accelerate development. However, ensure you read and understand generated code thoroughly. If you don’t understand, don’t use it. At the end of the day, if you generate a lot of code and face errors or unexpected behavior, you will never truly be in control of the code.

* **Cursor IDE:** [Cursor](https://cursor.com/)  
* **Claude Code:** [Claude Code](https://claude.com/product/claude-code)

---

# Machine Learning Foundations

### General ML/AI Basics

Build or refresh your foundational machine learning concepts.

* **Introduction Course:** [Coursera Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

### Scientific Machine Learning (SciML)

We leverage SciML for physics-consistent learning and model interpretability.

* **SciML Modules:** [Scientific ML Overview](https://kks32-courses.github.io/sciml/index.html)

---

# Topic-Specific Learning Materials

## Graph Neural Networks (GNNs)

We use graphs for physics-aware learning and physical simulations.

* **Introduction:** [A Gentle Introduction to Graph Neural Networks](https://distill.pub/2021/gnn-intro/)

### Graph Neural Simulators (GNS)

GNNs applied to physics-informed learning, such as granular flow simulations.

* **Paper:** [GNS Paper (Computers and Geotechnics)](https://doi.org/10.1016/j.compgeo.2023.106015)  
* **Code Repository:** [GeoElements GNS Repository](https://github.com/geoelements/gns)

### Neural Operators

Fast physics-aware surrogate modeling for high-fidelity simulations (e.g., FEM, MPM).

* **DeepONet:** [DeepONet Module](https://kks32-courses.github.io/sciml/02-deeponet/deeponet.html)  
* **Fourier Neural Operator (FNO):** [FNO Module](https://kks32-courses.github.io/sciml/05-fno/fno.html)

### Agentic AI & Workflow Engineering

* **Agentic Design:** Tailor AI agents to streamline research workflows.  
* **Frameworks:** Develop custom multi-agent applications using LangChain and LangGraph.