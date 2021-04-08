.. METINTOS documentation master file, created by
   sphinx-quickstart on Sun Feb 17 20:11:10 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

METeorological INterpolation Toolbox for Optimization and Simulation (METINTOS)
===============================================================================

What is METINTOS?
-----------------
METINTOS is a libray that interpolates meteorological variables in time.
It is distributed under the GNU Lesser General Public License v3.0.

**Citation info**: D. Daniel González-Arribas, J. García-Heras, M. Soler and E.A. Enderiz, METeorological INterpolation Toolbox for Optimization and Simulation (METINTOS) an open source meteorological variable interpolator.

How to run the library
----------------------

1. Clone or download the repository.
2. Install all the dependencies.


How to use it
-------------

1. From your meteorological files you have to create the dataset, you have to use xarray.open_mfdataset, you can obtain information in the xarray documentation ([xarray.open_mfdataset link](http://xarray.pydata.org/en/stable/generated/xarray.open_mfdataset.html)).


::

    ds = xr.open_mfdataset(files, engine='h5netcdf', concat_dim=['step'], combine='nested')


2. Create the DatasetHandler calling metintos.io.DatasetHandler.

::

    dsh = metintos.io.DatasetHandler(cls.ds)


3. Create CoordinateGenerator object and new axis, i.e.: latitudes, longitudes, steps.

::

    cg = metintos.io.CoordinateGenerator()
    cg.add_axis_lims_n_points('latitude', l0, lf, ls)
    cg.add_axis_lims_n_points('longitude', lo0, lof, los)
    cg.add_axis_lims_resolution('step', s0, sf, ss)


4. Produce the new dataset interpolated with optical flow

::

    dsn = dsh.get_optical_flow_interpolated_dataset(cg.axes)




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
   
   
   