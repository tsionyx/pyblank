#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The main distribution file of a package.

Some ideas borrowed from https://github.com/kennethreitz/setup.py

Note: To use the 'upload' functionality of this file, you must:
$ pip install twine
"""

from __future__ import unicode_literals, print_function

import io
import os
import sys
from shutil import rmtree

from setuptools import (
    setup,
    find_packages,
    Command,
)
# noinspection PyPep8Naming
from setuptools.command.test import test as TestCommand

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(file_name, base_dir=CURRENT_DIR):
    with io.open(os.path.join(base_dir, file_name), encoding='utf-8') as f:
        return '\n' + f.read()


# Package meta-data.
ME = 'tsionyx'

# Do not rely on the current dir: it fails when install from sources
# NAME = os.path.basename(CURRENT_DIR)
NAME = 'pyblank'
DESCRIPTION = 'Blank Python Project'
URL = 'https://github.com/{}/{}'.format(ME, NAME),
EMAIL = '{}@gmail.com'.format(ME)
AUTHOR = ME
LICENSE = 'MIT License'

REQUIRED = [
    'six',
]

# http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-extras-optional-features-with-their-own-dependencies
REQUIRED_EXTRAS = {
}

TEST_WITH = [
    'flake8',
    'pytest',
    'coverage',
    'tox',
]

KEYWORDS = [
    'empty',
]

CLASSIFIERS = [
    # Trove classifiers
    # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
]

# Load the package's __version__.py module as a dictionary.
about = {}
exec(read_file(os.path.join(NAME, '__version__.py')), about)

VERSION = about['__version__']
DOWNLOAD_URL = 'https://pypi.python.org/pypi/{}/{}'.format(NAME, VERSION),
SCRIPTS = [
    # '{0}={0}.__main__:main'.format(NAME),
]


class ToxTest(TestCommand):
    description = 'Run tests with tox'

    user_options = []

    def initialize_options(self):
        pass

    @classmethod
    def finalize_options(cls):
        if 'test' in sys.argv:
            sys.argv.remove('test')

    def run(self):
        self.install_dists(self.distribution)

        # noinspection PyUnresolvedReferences,PyPackageRequirements
        import tox
        tox.cmdline()


class UploadCommand(Command):
    """
    Support setup.py upload.

    https://github.com/kennethreitz/setup.py/blob/master/setup.py
    """

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds')
            rmtree(os.path.join(CURRENT_DIR, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine')
        os.system('twine upload dist/*')

        sys.exit()


if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        packages=find_packages(exclude=('tests',)),
        install_requires=REQUIRED,

        # INCLUDING DATA FILES:
        # http://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
        include_package_data=True,

        # examples should ship with the package
        # package_data={
        #     # explicitly str, not unicode
        #     # https://github.com/myint/language-check/issues/30
        #     str(NAME): ['examples/*.txt'],
        # },

        # LICENSE and docs are listed in MANIFEST.in
        # so they will be included in source distribution
        # but excluded from installation
        exclude_package_data={
            # explicitly str, not unicode
            # https://github.com/myint/language-check/issues/30
            str(''): ['LICENSE', '*.md']
        },
        # As it appears these files are not included in any package
        # so they will be excluded anyway. However i kept this to be more verbose.

        # REQUIREMENTS:
        extras_require=REQUIRED_EXTRAS,
        tests_require=TEST_WITH,
        entry_points={
            'console_scripts': SCRIPTS,
        },

        # PyPI metadata
        author=AUTHOR,
        author_email=EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        keywords=KEYWORDS,
        url=URL,
        download_url=DOWNLOAD_URL,

        long_description=read_file('README.rst'),
        classifiers=CLASSIFIERS,
        cmdclass={
            'test': ToxTest,
            'upload': UploadCommand,
        }
    )
