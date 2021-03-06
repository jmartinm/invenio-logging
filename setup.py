# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Module providing logging capabilities."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'blinker>=1.4',
    'check-manifest>=0.25',
    'coverage>=4.0',
    'flask-celeryext>=0.2.0',
    'flask-login>=0.3.2',
    'httpretty>=0.8.14',
    'isort>=4.2.2',
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.2',
    ],
    'tests': tests_require,
    'sentry': [
        'raven[flask]>=5.0.0',
        'celery>=3.1.0',
    ]
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7.0',
]

install_requires = [
    'Flask>=0.11.1',
    'six>=1.10.0',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_logging', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-logging',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio logging',
    license='GPLv2',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-logging',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'invenio_logging_fs = invenio_logging.fs:InvenioLoggingFS',
            'invenio_logging_sentry'
            ' = invenio_logging.sentry:InvenioLoggingSentry',
            'invenio_logging_console'
            ' = invenio_logging.console:InvenioLoggingConsole',
        ],
        'invenio_base.api_apps': [
            'invenio_logging_fs = invenio_logging.fs:InvenioLoggingFS',
            'invenio_logging_sentry'
            ' = invenio_logging.sentry:InvenioLoggingSentry',
            'invenio_logging_console'
            ' = invenio_logging.console:InvenioLoggingConsole',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 4 - Beta',
    ],
)
