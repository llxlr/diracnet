import unittest
from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'absl-py', 'kfac>=0.2.3', 'numpy<1.19.0', 'pandas', 'pyscf', 'pyblock',
    'dm-sonnet<2.0', 'tables', 'torch>=1.0',
    'tensorflow_probability==0.8'
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
    version='0.1',
    description='',
    url='https://github.com/llxlr/diracnet',
    author='llxlr',
    author_email='i@xhlr.top',
    # Contained modules and scripts.
    #scripts=['diracnet'],
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRA_PACKAGES,
    platforms=['any'],
    license='MIT License',
    test_suite='setup.diracnet_test_suite',
)
