from setuptools import setup, find_packages


NAME = "accio-client"
VERSION = "0.0.1"
DESCRIPTION = "Accessible IO Client Tool"
LONG_DESCRIPTION = """
Accessible IO Client Tool
"""
ENTRY_POINTS = {
    "console_scripts": [
        "accio = accio.cli:main",
    ]
}
AUTHOR = "Jaehyun Sim"
AUTHOR_EMAIL = "simjay@simjay.com"
KEYWORD = "accio, accessible, io"
LICENSE = "Apache License 2.0"
URL = "https://github.com/simjay/accio-client"
DOWNLOAD_URL = ""
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
]
PYTHON_REQUIRES = ">=3.6"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION
    packages = find_packages(),
    install_requires=requirements,
    python_requires=PYTHON_REQUIRES,
    entry_points=ENTRY_POINTS,
    author=AUTHOR,
    keyword=KEYWORD,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    dependency_links=dependency_links,
    author_email=AUTHOR_EMAIL,
    classifiers=CLASSIFIERS
)