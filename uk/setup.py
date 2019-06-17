import os
import sys

from setuptools import setup, find_packages

setup(
  name='uk',
  version='1.0',
  description='Testing the Pack',
  author='Uttam Kumar',
  author_email='uttamaot@gmail.com',
  url='https://github.com/uttam930/uttam.git',
  packages=find_packages(),
  scripts=[],
  data_files=[],
  # keep requires as light as possible to allow easy importing
  install_requires=['mock', 'pyyaml','sqlalchemy'],
  #dependency_links=['http://acc-pypi.cisco.com:8080/simple/sia']
)
