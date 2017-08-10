#!/usr/bin/env python
from setuptools import setup

setup(name='tidex-api',
      version='0.9',
      author='CodeReclaimers, LLC',
      author_email='alan@codereclaimers.com',
      url='https://github.com/lromanov/tidex-api',
      license="MIT",
      description='A library for the public and private APIs of the digital currency trading site tidex.com.',
      packages=['tidexapi'],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: PyPy',
      ]
      )
