apn-formats
===========
This package is meant to validate or lookup Assessor's Parcel Number (APN) formats for any given state/county in the United States.

|Build Status|

Getting Started
---------------
To get started, install the package: ::

    pip install apn

Prerequisites
-------------
- python 2.7
- `fuzzywuzzy <https://pypi.python.org/pypi/fuzzywuzzy>`__
- `python-Levenshtein <https://pypi.python.org/pypi/python-Levenshtein/0.12.0>`__


Examples
--------
Lookup formats: ::

    >> import apn
    >> apn.lookup(state='WA')
    {'WA': {'King': ['XXXXXX-XXXX', 'XXXXXXXX', 'XXXXXX-XXXXSXX'], 'Snohomish': ['XXXXXXXXXXXXXX','XXXXXXX'], ...}}
    >> apn.lookup(state='WA', county='King')
    {'WA': {'King': ['XXXXXX-XXXX', 'XXXXXXXX', 'XXXXXX-XXXXSXX']}}
    >> apn.lookup()
    {'WA': {'King': ['XXXXXX-XXXX', 'XXXXXXXX', 'XXXXXX-XXXXSXX'], ...}, 'CA': {...}, ...}

Validate APN: ::

  >> import apn
  >> apn.validate(apn_input='123456-1234') # Search every counties' APN format
  [<APN:XXXXXX-XXXX>, ...]
  >> apn.validate(apn_input='123456-1234', state='WA')
  [<APN:XXXXXX-XXXX>]
  >> apn.validate(apn_input='123456-1234', state='WA', county='King')
  [<APN:XXXXXX-XXXX>]
  >> apn.validate(apn_input='123456-1234', state='Washington')
  [<APN:XXXXXX-XXXX>]
  >> apn.validate(apn_input='123456-1234', state='washngton')
  [<APN:XXXXXX-XXXX>]


Errors
------
The following uses cases are events in which an error will be thrown:

- County but not state is provided
- County name does not match our validation methods (see below)
- County does not exist in the given state
- State name does not match our validation methods (see below)
- State abbrev is incorrect
- APN regex formula is invalid
- APN format doesn't match the given state/county


Validation Method
-----------------
We're using the string match library, *fuzzywuzzy*, to determine a certainty level against
State (full name) and County names. We'll handle the name matching if you wish to use this
against direct user input, however be **warned** that our certainty level is arbitrary to
our judgement and the use cases we've encountered. It is always a best practice to validate
user input yourself.

Contributing
------------
Contributions are welcome, but I doubt anyone will be interested in using this package.
We're currently storing our data in a SQLite3 database, *apn.db*. If you make updates to this database
please run the *build.py* script to re-pickle the data.

Authors
-------
- **Eric Proulx** - *Owner* - `Website <http://www.ericproulx.com/>`__
- **Ken Harmon** - *Owner* - `Website <https://kenharmon.net/>`__

License
-------
This project is licensed under the MIT License - see the `LICENSE <https://github.com/dogpackdesign/apn-formats/blob/master/LICENSE>`__ file for details

Changelog
---------

.. |Build Status| image:: https://travis-ci.org/dogpackdesign/apn-formats.svg?branch=master
   :target: https://travis-ci.org/profile/dogpackdesign
