# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-adapters',
    packages=['adapters'],
    version='2.1.0',
    description='Python adapters',
    author='Alexei',
    author_email='hello@alexei.ro',
    url='https://github.com/alexei/python-adapters',
    download_url='https://github.com/alexei/python-adapters/archive/2.1.0.tar.gz',  # noqa
    keywords=['adapter pattern'],
    install_requires=[
        'future',
        'python-dateutil>=2.7.0',
        'six>=1.13.0',
    ],
)
