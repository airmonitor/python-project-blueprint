
from setuptools import setup, find_packages
from os import environ

import blueprint

with open("README.rst") as readme:
    long_description = readme.read()

setup(
    author="",
    author_email="",
    long_description=long_description,
    long_description_context="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    license="GNU GENERAL PUBLIC LICENSE",
    name="blueprint",
    packages=list(find_packages("blueprint", exclude=["*test*"])),
    url="",
    version=environ["version"],
)
