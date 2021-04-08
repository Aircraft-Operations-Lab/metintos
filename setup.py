#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
  name = 'metintos',         # How you named your package folder (MyLib)
  packages = ['metintos'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='lgpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Meteorological Interpolation Toolbox for Optimization and Simulation',   # Give a short description about your library
  author = 'Daniel González Arribas',                   # Type in your name
  author_email = 'dangonza@ing.uc3m.es',      # Type in your E-Mail
  url = 'https://github.com/javiergarciaheras/mitos',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/javiergarciaheras/mitos/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Optical flow', 'Meteorological', 'Interpolation', 'Optimization', 'Simulation'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'xarray',
          'numpy',
          'casadi',
          'scipy',
          'hyperopt',
          'setuptools'
      ],
  extras_require={
          'tuning': ['hyperopt'],
      },
  include_package_data=True,
  tests_require=["pytest"],
  zip_safe=False,
  classifiers=[ # Chose the classifiers from here: https://pypi.org/classifiers/
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Science/Research',      # Define that your audience are developers
    'Intended Audience :: Education',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',   # Again, pick a license
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5', #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)