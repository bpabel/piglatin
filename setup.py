import sys
import os
import io
from typing import List, Dict
from setuptools import setup, find_packages


# Package meta-data.
NAME = "piglatin"
DESCRIPTION = "Converts text to piglatin."
URL = "https://github.com/bpabel/piglatin"
EMAIL = "007brendan@gmail.com"
AUTHOR = "Brendan Abel"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = None
REQUIRED: List[str] = []

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
about: Dict[str, str] = {}
if not VERSION:
    with open(os.path.join(here, NAME, "_version.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
