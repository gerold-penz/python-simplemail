#!/usr/bin/env python
# coding: utf-8
"""
Python-Simplemail - Setup
 
Created
    2013-02-02 by Gerold - http://halvar.at/
"""

import os
from setuptools import setup, find_packages, findall

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = "https://code.google.com/p/python-simplemail/"
DOWNLOAD_BASEURL = "https://python-simplemail.googlecode.com/files/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "python-simplemail-%s.tar.gz" % VERSION


setup(
#    install_requires = [],
    name = "python-simplemail",
    version = VERSION,
    description = (
        "Python Module To Send Emails"
    ),
    long_description = open("README.txt").read(),
    keywords = "email simplemail send attachments e-mail",
    author = "Gerold Penz",
    author_email = "gerold@halvar.at",
    url = HOMEPAGE,
    download_url = DOWNLOAD_URL,
    packages = find_packages(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Communications :: Email",
    ],
)

