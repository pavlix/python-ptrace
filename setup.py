#!/usr/bin/env python

# Produce to release a new version:
#  - git pull --rebase  # check that there is no incoming changesets
#  - run tests, type: tox
#  - check version in ptrace/version.py and doc/conf.py
#  - set release date in the ChangeLog
#  - check that "python setup.py sdist" contains all files tracked by
#    the SCM (Mercurial): update MANIFEST.in if needed
#  - git commit -a
#  - git push
#
#  - git tag python-ptrace-x.y
#  - git push --tags
#
#  - ./setup.py sdist register bdist_wheel upload
#  - update the doc
#  - increment version in  ptrace/version.py and doc/conf.py
#  - git commit
#  - git push

from __future__ import with_statement

from imp import load_source
from os import path
try:
    # setuptools supports bdist_wheel
    from setuptools import setup
except ImportError:
    from distutils.core import setup


MODULES = ["ptrace", "ptrace.binding", "ptrace.syscall", "ptrace.debugger"]

SCRIPTS = ("strace.py", "gdb.py")

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]

with open('README.rst') as fp:
    LONG_DESCRIPTION = fp.read()

ptrace = load_source("version", path.join("ptrace", "version.py"))
PACKAGES = {}
for name in MODULES:
    PACKAGES[name] = name.replace(".", "/")

install_options = {
    "name": ptrace.PACKAGE,
    "version": ptrace.VERSION,
    "url": ptrace.WEBSITE,
    "download_url": ptrace.WEBSITE,
    "author": "Victor Stinner",
    "description": "python binding of ptrace",
    "long_description": LONG_DESCRIPTION,
    "classifiers": CLASSIFIERS,
    "license": ptrace.LICENSE,
    "packages": list(PACKAGES.keys()),
    "package_dir": PACKAGES,
    "scripts": SCRIPTS,
}

setup(**install_options)
