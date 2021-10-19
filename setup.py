# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path
# The directory containing this file
HERE = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="Polar_codes_BEC",
    version="1.2.3",
    description="Polar_codes_BEC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/Polar-codes-BEC/",
    download_url="https://github.com/issamo-vitch/polar-codes/archive/refs/tags/v1.2.3-BEC.tar.gz",
    author="Issame EL KAIME and AIT MADI Abdessalam",
    author_email="issame.elkaime@uit.ac.ma",
    license="MIT",
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["Polar_codes_BEC"],
    include_package_data=True,
    install_requires=["numpy"]
)