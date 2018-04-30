# -*- coding: utf-8 -*-
#
import os
import codecs

from setuptools import setup, find_packages

# https://packaging.python.org/single_source_version/
base_dir = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(base_dir, 'optipy', '__about__.py'), 'rb') as f:
    # pylint: disable=exec-used
    exec(f.read(), about)


def read(fname):
    return codecs.open(os.path.join(base_dir, fname), encoding='utf-8').read()


setup(
    name='optipy',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=find_packages(),
    package_data={'optipy': ['data/journals.json']},
    description='Numerical optimization/minimization',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url=about['__website__'],
    license=about['__license__'],
    platforms='any',
    install_requires=[
        'numpy',
        'scipy',
        ],
    classifiers=[
        about['__status__'],
        about['__license__'],
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        ],
    )
