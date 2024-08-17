#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="CNV",
    version=__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
     'numpy>=1.21',
     'pandas>=1.3',
     'scikit-learn>=1.0.1',
     'plotly>=5.4',
     'pybedtools>=0.8.2',
     'importlib-resources',
     'joblib',
     'scipy>=1.6.0',
     'threadpoolctl>=3.1.0',
     'pysam',
     'python-dateutil>=2.8.2',
     'pytz>=2020.1',
     'tzdata>=2022.7'
    ],
    scripts=['script/ifCNV']
)
