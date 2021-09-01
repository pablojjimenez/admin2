#!/bin/bash

function usage {
    echo "==============================================================================="
    echo "usage: $0 [keyword]"
    echo "*   keyword:    test class name or test function name or test file name"
    echo "==============================================================================="
}

usage

# activate test environment
. test_venv/bin/activate

# run all the tests under the 'tests' folder
if [ "$1" != "" ]; then
  python -m pytest -v tests -k "$1"
else
  python -m pytest -v tests
fi

# deactivate virtual env
deactivate
