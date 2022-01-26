import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Cards",
    version = "0.0.0",
    author = "Ryan Barishian",
    author_email = "rgbarishian@gmail.com",
    description = ("A demonstration of OOP by making card games."),
    url = "https://github.com/rgbarishian/Cards",
    packages=['Cards'],
    long_description=read('README.md'),
)