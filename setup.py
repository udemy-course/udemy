#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='udemy',
    version='0.0.1',
    # packages=['udemy'],
    include_package_data=True,
    install_requires=['requests>=1.0'],
    entry_points={
        'console_scripts': [
            'udemy = udemy.cli:main'
        ]
    }
)
