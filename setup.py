#coding:utf-8

import os
from subprocess import check_call
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()


requires = [
    'nose',
    'setuptools>=1.0',
]


def unzip_library():
    os.chdir(os.path.join(here, 'genius/library'))
    check_call(['unzip', 'library.zip'])
    os.chdir(here)
unzip_library()


setup(

    name='genius',
    description='genius中文分词 Chinese Segment On linear-chain CRF',
    version='2.0.0',
    author='duanhongyi',
    author_email='duanhyi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=README + '\n\n' + CHANGES,
    install_requires=[
        'wapiti',
    ],
    dependency_links=[
        'git+https://github.com/duanhongyi/python-wapiti.git#egg=wapiti',
    ],
    platforms='all platform',
    license='BSD',
)
