# -*- coding: utf-8 -*-

from setuptools import setup

from pymadapi import __version__
from pymadapi import __license__
from pymadapi import __author__


with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='pymadapi',
    author=__author__,
    author_email="abolvah8@gmail.com",
    url='https://github.com/Team-MadBot/pyMadAPI',
    version=__version__,
    packages=['pymadapi', 'pymadapi.base', 'pymadapi.aio'],
    license=__license__,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    description='Python SDK for the MadAPI',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements
)
