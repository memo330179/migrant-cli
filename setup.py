"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from migrant import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name = 'migrant',
    version = __version__,
    description = 'A command line to create migration and run migrations',
    long_description = long_description,
    url = '',
    author = 'Guillermo Ramos',
    author_email = 'ramosmaciasg@gmail.com',
    license = 'UNLICENSE',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',

    ],
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt', 'termcolor'],
    extras_require = {
        
    },
    entry_points = {
        'console_scripts': [
            'migrant=migrant.cli:main',
        ],
    },
    cmdclass = {},
)