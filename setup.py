#!/usr/bin/env python
# coding: utf-8
"""
Python-Simplemail - Setup
 
Created
    2013-02-02 by Gerold - http://halvar.at/
"""

import os
from setuptools import setup, find_packages

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = "https://github.com/gerold-penz/python-simplemail"
DOWNLOAD_BASEURL = "https://github.com/gerold-penz/python-simplemail/raw/master/dist/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "python-simplemail-%s.tar.gz" % VERSION


setup(
    name = "python-simplemail",
    version = VERSION,
    description = (
        "Send Emails with Python - Simple SMTP Email Client Library"
    ),
    long_description = open("README.rst").read(),
    keywords = (
        "Email, Send, Attachments, E-Mail, SMTP, Client, Simplemail"
    ),
    author = "Gerold Penz",
    author_email = "gerold@halvar.at",
    url = HOMEPAGE,
    download_url = DOWNLOAD_URL,
    packages = find_packages(),
    classifiers = [
        # "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
)
