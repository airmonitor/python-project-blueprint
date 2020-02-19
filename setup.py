
from setuptools import setup
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# The text of the README file
with open(path.join(HERE, "README.rst")) as fid:
    long_description = fid.read()

with open(path.join(HERE, "VERSION")) as version_fh:
    version = version_fh.read()

setup(
    author="",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    license="GNU GENERAL PUBLIC LICENSE",
    name="blueprint",
    packages=["blueprint"],
    url="",
    version=version,
    include_package_data=True,
)
