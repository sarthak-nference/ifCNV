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
        "pybedtools>=0.8.2",
        "importlib-resources"
    ],
    scripts=['script/ifCNV']
)
