#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='mitos',
      version='0.1',
      description='Meteorological Interpolation Toolbox for Optimization and Simulation',
      author='Daniel González Arribas',
      author_email='dangonza@ing.uc3m.es',
      packages=['mitos'],
      install_requires=['xarray', 'numpy', 'casadi', 'scipy', 'hyperopt', 'setuptools'],
      extras_require={
            'tuning': ['hyperopt'],
      },
      include_package_data=True,
      zip_safe=False)
