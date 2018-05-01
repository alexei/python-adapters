# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='python-adapters',
    packages=['adapters'],
    version='2.0.1',
    description='Python adapters',
    author='Alexei',
    author_email='hello@alexei.ro',
    url='https://github.com/alexei/python-adapters',
    download_url='https://github.com/alexei/python-adapters/archive/2.0.1.tar.gz',  # noqa
    keywords=['adapter pattern'],
    install_requires=[
        'future',
        'python-dateutil>=2.6.0',
    ],
)
