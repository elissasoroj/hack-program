#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
Required packages:
PyObjC
playsound
csv
random
time
"""

from setuptools import setup

# build command
setup(
    name="sketchprompt",
    version="0.0.2",
    author="Elissa Sorojsrisom",
    author_email="ess2239@columbia.edu",
    license="GPLv3",
    description="A package to help you fill your sketchbook",
    install_requires = ["PyObjC", "playsound", "csv", "random", "time"],
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["sketchprompt = sketchprompt.__main__:main"]
    },
)
