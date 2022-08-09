#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md")) as f:
    long_description = f.read()


with open(path.join(this_directory, "requirements.txt")) as f:
    requirements = [x for x in f.readlines()]

setup(
    name="umlsmap2rdf",
    version="0.0.1",
    description="Quick and nasty script to get mapping out of MRCONSO.RRF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KeironO/umlsmap2rdf",
    author="KeironO",
    author_email="keiron.oshea@wales.nhs.uk",
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
        [console_scripts]
        umlsmap2rdf=umlsmap2rdf:cli
    """,
    install_requires = requirements
)