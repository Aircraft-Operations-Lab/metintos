# METeorological INterpolation Toolbox for Optimization and Simulation (METINTOS)

[![Build Status](https://app.travis-ci.com/Aircraft-Operations-Lab/metintos.svg?branch=master)](https://app.travis-ci.com/Aircraft-Operations-Lab/metintos)
[![GitHub](https://img.shields.io/github/license/javiergarciaheras/metintos)]()
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/javiergarciaheras/metintos)]()
[![Documentation Status](https://readthedocs.org/projects/metintos/badge/?version=latest)](https://metintos.readthedocs.io/en/latest/?badge=latest)
      
## What is METINTOS?

METINTOS is a library that interpolates meteorological variables in time.
It is distributed under the GNU Lesser General Public License v3.0.

**Citation info**: D. Daniel González-Arribas, J. García-Heras, M. Soler and E.A. Enderiz, METeorological Interpolation Toolbox for Optimization and Simulation (METINTOS) an open source meteorological variable interpolator.

## How to run the library

1. Clone or download the repository.
2. Install all the dependencies.


## How to use it

1. From your meteorological files, you have to create the dataset and use xarray.open_mfdataset, you can obtain information in the xarray documentation ([xarray.open_mfdataset link](http://xarray.pydata.org/en/stable/generated/xarray.open_mfdataset.html)).


```python
ds = xr.open_mfdataset(files, engine='h5netcdf', concat_dim=['step'], combine='nested')
```

2. Create the DatasetHandler calling metintos.io.DatasetHandler.

```python
dsh = metintos.io.DatasetHandler(cls.ds)
```

3. Create CoordinateGenerator object and new axis, i.e., latitudes, longitudes, steps.

```python
cg = metintos.io.CoordinateGenerator()
cg.add_axis_lims_n_points('latitude', l0, lf, ls)
cg.add_axis_lims_n_points('longitude', lo0, lof, los)
cg.add_axis_lims_resolution('step', s0, sf, ss)
```

4. Produce the new dataset interpolated with optical flow

```python
dsn = dsh.get_optical_flow_interpolated_dataset(cg.axes)
```

## How to compile documentation pdf


You can use the Makefile created by Sphinx to create your documentation. Locate yourself in the documentation path.

First, clean the _build directory to avoid errors or legacy information. Just call:

```bash
make clean
```

In case you want to build your documentation in latex, call **twice**:

```bash
make latexpdf
```

If you want to build your HTML call:

```bash
make html
```

Note that you **should not see** any error or warning; this information appears as red text in the terminal.




## Contents


Check METINTOS documentation in the following link: [METINTOS documentation link](https://metintos.readthedocs.io/en/latest/).



## Acknowledmgements



This library has been developed within [FMP-Met Project](https://fmp-met.com). *FMP-Met has received funding from the SESAR Joint Undertaking (JU) under grant agreement No 885919. The JU receives support from the European Union’s Horizon 2020 research and innovation programme and the SESAR JU members other than the Union*.

   
   
   
