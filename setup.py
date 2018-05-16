#!/usr/bin/env python

from distutils.core import setup

setup(name='layoutmargin',
      version='20180517',
      description='Mixins that adds margin functionality to Kivy widgets',
      author='Andre Miras',
      url='https://github.com/AndreMiras/garden.layoutmargin',
      packages=['layoutmargin'],
      package_data={'layoutmargin': ['*.kv']},
      install_requires=['kivy'])
