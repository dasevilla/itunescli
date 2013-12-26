from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='itunescli',
    version='0.1.0',

    description='Command line tool to query the iTunes search API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/itunescli',
    download_url='https://github.com/dasevilla/itunescli/tarball/master',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],

    install_requires=[
        'cliff',
        'cliff-tablib',
        'python-itunes',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'itunescli = itunescli.main:main'
        ],
        'itunescli': [
            'search = itunescli.query:SearchLister',
            'show = itunescli.query:SearchOne',
            'artwork = itunescli.query:GetArtwork',
        ],
    },
)
