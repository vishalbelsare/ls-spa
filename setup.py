#!/usr/bin/python
from setuptools import setup, find_packages

setup(
    name="ls_spa",
    version="1.0.0",
    setup_requires=["setuptools>=18.0"],
    packages=find_packages(exclude=["notebooks"]),
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
    ],
    description="Efficient Shapley performance attribution for least-squares problems",
    url="https://github.com/cvxgrp/ls-spa",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
    ],
    python_requires=">=3.10",
)
