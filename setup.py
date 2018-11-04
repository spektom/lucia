#!/usr/bin/env python

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='lucia',
    version='0.1',
    use_scm_version=True,
    description='Lucia',
    long_description=README,
    author='Michael Spector',
    author_email='spektom@gmail.com',
    url='http://luciathefriend.com',
    license='Proprietary',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=requirements,
    packages=find_packages(),
    entry_points={'console_scripts': ['lucia = lucia.app:main']},
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest'],
    test_suite='tests',
    zip_safe=False,
)
