.. kubem documentation master file, created by
   sphinx-quickstart on Fri Mar  5 14:23:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation for kubem
=======================

``kubem`` is a Python library to read, process and analyze building 
energy dataframes for cities in Chile. 
Inverse modeling simulation is performed through the `BETTER`_ library.
Additional routines are implemented for analysis and visualization of
data through the web-based plattform `CityBES`_.

The library is being develeped and maintaned by the `Kipus`_ Software 
Team at University of Talca.

.. _BETTER: https://github.com/LBNL-JCI-ICF/better
.. _CityBES: https://citybes.lbl.gov/#menu0
.. _KIPUS: https://www.kipus.cl

.. toctree::
   :maxdepth: 1
   :caption: Contents

   install

.. toctree::
   :maxdepth: 2
   :caption: Modules

   main_module
   io_module
   geo_module
   utils_module

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
