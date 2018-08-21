__author__ = 'asafe'
import pytest

from distutils.core import setup

setup(
    name='crawler-challenge',
    version='1.0',
    description='crawler challenge',
    author='asafe',
    author_email='asafeao@if.uff.br',
    url='https://github.com/asafepy/crawler-challenge.git',
    packages=[
      'core',
      'core.db',
      'core.modules',
      'core.utils',
      'config',
    ],
)