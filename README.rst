Command-line interface to query the `iTunes Search API
<http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-
web-service-search-api.html>`_. Relies on the `python-itunes
<http://pypi.python.org/pypi/python-itunes>`_ and `cliff
<http://pypi.python.org/pypi/cliff>`_ libraries.

==================
 Running itunescli
==================

Usage
-----

::

    $ itunes -h
    usage: itunes [--version] [-v] [-q] [-h] [--debug]

    Query the iTunes search API

    optional arguments:
    --version      show program's version number and exit
    -v, --verbose  Increase verbosity of output. Can be repeated.
    -q, --quiet    suppress output except warnings and errors
    -h, --help     show this help message and exit
    --debug        show tracebacks on errors

    Commands:
    artwork        Get the album artwork from the first result of a query
    help           print detailed help for another command
    search         Search iTunes
    show           Show the first result from a search query
