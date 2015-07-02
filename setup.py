#!/usr/bin/env python3

from setuptools import setup, find_packages
from myenv import VERSION
setup(
    name = "myenv",
    version = VERSION,
    packages = find_packages(),
    scripts = ['myenv.py'],

    entry_points = {
        'console_scripts': [
            'myenv = myenv:main',
        ]
    }
)