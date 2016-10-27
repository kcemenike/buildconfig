# -*- coding: utf8 -*-

#from distutils.core import setup, find_packages
from setuptools import setup, find_packages

setup(
    name = 'buildconfig',
    packages=find_packages(exclude=('buildconfig.yaml.*')),
    scripts=['bin/buildconfig'],
    version = '0.2',
    description = '.buildconfig edit build integration tool',
    author = 'Moritz Möller',
    author_email = 'mm@mxs.de',
    url = 'https://github.com/mo22/buildconfig'
)
