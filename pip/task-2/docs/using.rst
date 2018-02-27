How to use it
=============

bin/ica
-------

The library is provided with a cli: `bin/ica`. To ask if an url is alive::

  $ ./bin/ica url

It should return "OK" if it is alive or "KO" if it is not.

examples
--------

A couple of cli call examples::

  $ ./bin/ica http://www.google.com
  OK

  $ ./bin/ica http://www.google.com/404
  KO

