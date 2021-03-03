# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in postal_hub/__init__.py
from postal_hub import __version__ as version

setup(
	name='postal_hub',
	version=version,
	description='Add the data entry from the API and retrieve accordingly',
	author='kavin',
	author_email='kavinkumarnkm007@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
