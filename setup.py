#!/usr/bin/env python
# -*- coding: utf8 -*-

from io import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "django-iso8601",
    description = u"Django tools for working with ISO 8601",
    long_description=long_description,
    long_description_content_type='text/plain',
    url = u"http://github.com/k0001/django-iso8601",
    author = u"Renzo Carbonara",
    author_email = u"gnuk0001@gmail.com",
    license = u"BSD",
    keywords = "django iso8601 dates times datetime fields validation",

    zip_safe = True,
    include_package_data = True,

    packages = find_packages(
        exclude=['tests']
    ),

    # Use setuptools_scm to take a version from git tags
    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    install_requires = [
        'Django>=1.10',
        'isodate>=0.4',
    ],

    test_suite = 'tests.test_suite',

    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]

)

