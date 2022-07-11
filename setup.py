#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

import os
import sys
import codecs
import subprocess

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


if sys.argv[-1] == "publish":
    subprocess.call(f"{sys.executable} setup.py sdist bdist_wheel upload", shell=False)
    sys.exit()

required = [""]

setup(
    name="emc_git",
)
