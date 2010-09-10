#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

setup(
    name = "django-iso8601",
    version = "0.1alpha2",
    description = u"Django tools for working with ISO 8601",
    url = u"http://github.com/k0001/django-iso8601",
    author = u"Renzo Carbonara",
    author_email = u"gnuk0001@gmail.com",
    license = u"BSD",
    keywords = "django iso8601 dates times",

    zip_safe = True,
    include_package_data = True,

    packages = find_packages(
        exclude=['tests']
    ),

    install_requires = [
        'Django>=1.0',
        'isodate>=0.4',
    ],

    test_suite = 'tests.test_suite',

    classifiers = [
        "Development Status :: 3 - Alpha",
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
    ]

)

