#!/usr/bin/env python

PROJECT = 'itunescli'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Command line tool to query the iTunes search API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/itunescli',
    download_url='https://github.com/dasevilla/itunescli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=['distribute_setup.py'],

    provides=[],
    install_requires=['distribute', 'cliff', 'python-itunes'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'itunes = itunescli.main:main'
            ],
        'itunes.search': [
            'search = itunescli.query:SearchLister',
            'show = itunescli.query:SearchOne',
            'artwork = itunescli.query:GetArtwork',
            ],
        },

    zip_safe=False,
    )
