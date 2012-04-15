#!/usr/bin/env python

from setuptools import setup

setup(name='postpress',
      version='0.1',
      description='A web application to display job postings integrated into your website.',
      author='Alfred Gutierrez',
      author_email='alf.g.jr@gmail.com',
      packages=['postpress'],
      install_requires=['Flask', 'flask-sqlalchemy']
)

