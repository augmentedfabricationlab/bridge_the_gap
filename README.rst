============================================================
bridge_the_gap: bridge_the_gap
============================================================

.. start-badges

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
    :target: https://github.com/augmentedfabricationlab/bridge_the_gap/blob/master/LICENSE
    :alt: License MIT

.. image:: https://travis-ci.org/augmentedfabricationlab/bridge_the_gap.svg?branch=master
    :target: https://travis-ci.org/augmentedfabricationlab/bridge_the_gap
    :alt: Travis CI

.. end-badges

.. Write project description

**A short description of the project** ...


Main features
-------------

* feature
* feature
* more features

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

* [CEM](https://github.com/OleOhlbrock/CEM
* [COMPAS](https://compas-dev.github.io/)
* [COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)
* [Assembly Information Model](https://github.com/augmentedfabricationlab/assembly_information_model)
* [AM Information Model](https://github.com/augmentedfabricationlab/am_information_model)
* [UR Fabrication Control](https://github.com/augmentedfabricationlab/ur_fabrication_control)


Getting Started
------------

### 1. Setting up the Anaconda environment with COMPAS and installing Dependencies

Follow the installation guide in the [le-ar-n](https://github.com/le-ar-n/le-ar-n) repository. You may skip AM Information Model.

### 2. Installting CEM

* Clone the [CEM](https://github.com/OleOhlbrock/CEM) repository into your projects folder.
* Copy the content of the folder CEM/CEM_180/CEM_180_Rhino6_GHPlugin folder (or the CEM/CEM_200/CEM_200_Rhino7_GHPlugin in case you are using Rhino 7) into the Components Folder of Grasshopper (File --> Special Folders --> Components Folder).


Contributing
------------

Make sure you setup your local development environment correctly:

* Clone the `bridge_the_gap <https://github.com/augmentedfabricationlab/bridge_the_gap>`_ repository.
* Install development dependencies and make the project accessible from Rhino:

::

    pip install -r requirements-dev.txt
    invoke add-to-rhino

**You're ready to start working!**

During development, use tasks on the
command line to ease recurring operations:

* ``invoke clean``: Clean all generated artifacts.
* ``invoke check``: Run various code and documentation style checks.
* ``invoke docs``: Generate documentation.
* ``invoke test``: Run all tests and checks in one swift command.
* ``invoke add-to-rhino``: Make the project accessible from Rhino.
* ``invoke``: Show available tasks.

For more details, check the `Contributor's Guide <CONTRIBUTING.rst>`_.


Releasing this project
----------------------

.. Write releasing instructions here


.. end of optional sections
..

Credits
-------------

This package was created by Julian Trummer <julian.trummer@tum.de> `@JulianTrummer <https://github.com/JulianTrummer>`_ at `@augmentedfabricationlab <https://github.com/augmentedfabricationlab>`_
