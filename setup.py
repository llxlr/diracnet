from setuptools import find_packages
from setuptools import setup
import unittest

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

REQUIRED_PACKAGES = [
    'numpy<1.19.0', 'pandas',
    'torch>=1.0',
]
EXTRA_PACKAGES = {
    'torch': ['torch>=1.0'],
}


def dirac_test_suite():
  test_loader = unittest.TestLoader()
  test_suite = test_loader.discover('diracnet/tests', pattern='*_test.py')
  return test_suite


setup(
    name='diracnet',
    version='0.0.5',
    description='Pseudo implementation of Ferminet based on PyTorch | 基于PyTorch的Ferminet伪实现',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/llxlr/diracnet',
    author='llxlr',
    author_email='i@xhlr.top',
    # Contained modules and scripts.
    #scripts=['bin/diracnet'],
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRA_PACKAGES,
    platforms=['any'],
    license='Apache 2.0',
    test_suite='setup.diracnet_test_suite',
)
