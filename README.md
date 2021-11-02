# Bridge the Gap

**Quick links:** [compas docs](https://compas-dev.github.io/main/) | [compas_fab docs](https://gramaziokohler.github.io/compas_fab/latest/) | [le-ar-n](https://github.com/le-ar-n/le-ar-n) | [CEM](https://github.com/OleOhlbrock/CEM) | [Karamba](https://www.karamba3d.com/)


**This repository provides an examplatory workflow for designing and assembling a truss structure.**


Main features
-------------

* Topological Formfinding
* Structural Analysis
* Robotic Assembly simulation

**bridge_the_gap** runs on Python 3.9 and compas_fab 0.19


Requirements
------------

* Windows 10 Professional
* Rhino 6 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)
* [Karamba 3D Free Version](https://www.karamba3d.com/)


Dependencies
------------

* [CEM](https://github.com/OleOhlbrock/CEM)
* [COMPAS](https://compas-dev.github.io/)
* [COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)
* [Assembly Information Model](https://github.com/augmentedfabricationlab/assembly_information_model)
* [UR Fabrication Control](https://github.com/augmentedfabricationlab/ur_fabrication_control)


Getting Started
------------

* Clone this repository to your PC via Github Desktop.

**1. Setting up the Anaconda environment with COMPAS and installing Dependencies**

* Follow the installation guide in the [le-ar-n](https://github.com/le-ar-n/le-ar-n) repository. (you may skip installing the AM Information Model)

**2. Installing CEM**

* Clone the [CEM](https://github.com/OleOhlbrock/CEM) repository into your projects folder.
* Copy the content of the folder "CEM/CEM_180/CEM_180_Rhino6_GHPlugin" (or "CEM/CEM_200/CEM_200_Rhino7_GHPlugin" in case you are using Rhino 7) into the Components Folder of Grasshopper (File --> Special Folders --> Components Folder) and restart Rhino.

**3. Installing Karamba**

* Go to the [Karamba](https://www.karamba3d.com/) website and download the Free (not the trial!) version.

**4. Installing Bridge_the_Gap**
::

    (learn) python -m pip install git+https://github.com/augmentedfabricationlab/bridge_the_gap@main#egg=bridge_the_gap
    (learn) python -m compas_rhino.install -p bridge_the_gap


Credits
-------------

This package was created by Julian Trummer <julian.trummer@tum.de> `@JulianTrummer <https://github.com/JulianTrummer>`_ at `@augmentedfabricationlab <https://github.com/augmentedfabricationlab>`_
