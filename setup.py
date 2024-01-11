#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='drf_orjson',
    version='2.0.3',
    python_requires=">=3.6",
    description='Django Rest Framework ORJSON Renderer',
    author='Gizmag,baffolobill',
    url='https://github.com/baffolobill/drf-orjson-renderer',
    packages=find_packages(exclude=["tests"]),
    install_requires=["django<3.0", "orjson", "djangorestframework"],
    extras_require={"dev": ["pytest", "pytest-runner", "pytest-cov", "pytest-mock"]},
)
