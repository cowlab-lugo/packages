How to run the tests
====================

python setup.py test
--------------------

Testing tool depends on *py.test* as we can see in the *setup.cfg*::

  [aliases]
  test=pytest
  [tool:pytest]
  addopts = --verbose --pep8 --cov iscowalive
  python_files = tests/test_*.py

The `python setup.py test` command is an alias of `pytest --verbose --pep8
--cov iscowalive` so you can run both::

  $ python setup.py test
  $ pytest --verbose --pep8 --cov iscowalive