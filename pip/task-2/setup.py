#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

version = '0.1'
readme = open('README.md').read()
requires = ['Requests', 'validators']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='iscowalive',
    version=version,
    author='Óscar M. Lage',
    author_email='info@oscarmlage.com',
    url='https://github.com/cowlab/iscowalive',
    description="""simple module that checks if url is available.""",  # noqa
    test_suite="runtests.run_tests",
    long_description=readme,
    scripts=['bin/ica'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    license="BSD",
)
