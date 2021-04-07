.. MITOS documentation master file, created by
   sphinx-quickstart on Sun Feb 17 20:11:10 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Meteorological Interpolation Toolbox for Optimization and Simulation (MITOS)
============================================================================

What is MITOS?
--------------
MITOS is a libray that interpolate meteorological variables in time.

How to install dependencies?
----------------------------
Needed libraries are listed on requirements.txt files.


How to use it?
--------------
(TBC)


How to compile documentation pdf?
---------------------------------

You can use the Makefile created by Sphinx to create your documentation. Locate yourself in the documentation path.

First clean the _build directory to avoid error or legacy information. Just call:

::

    make clean

In case you want to build your documentation in latex call **twice**:

::

    make latexpdf

if you want to do build your in html call:

::

    make html

Note that you **should not see** any error or warning, this information appears as red text in the terminal.




Contents
--------
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   code


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Acknowledmgements
-----------------
.. image:: images/fmp-met_logo.png
  :width: 100
  :align: center
  :alt: FMP-Met project

*This library has been developed within FMP-Met Project. FMP-Met has received funding from the SESAR Joint Undertaking (JU) under grant agreement No 885919. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and the SESAR JU members other than the Union*.
 
 
      ======    ======
      |pic1|    |pic2|
      ======    ======


.. |pic1| image:: images/european-union_flag_yellow_high.jpg
   :width: 50
   :alt: European Union

.. |pic2| image:: images/sesar.png
   :width: 50
   :alt: Sesar JU
   
   
   