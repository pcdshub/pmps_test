# pmps_test

[![travis-ci](https://img.shields.io/travis/pcdshub/pmps_test.svg)](https://travis-ci.org/pcdshub/pmps_test)        
[![pypi](https://img.shields.io/pypi/v/pmps_test.svg)](https://pypi.python.org/pypi/pmps_test)

Verify the functionality of the PMPS system via the ADS interface

## Dev Usage

After installing run the following command to see the basic tests:

`do_test`

To see an example of passing a parameter to the tests at runtime, run the following command:

`do_test --ams_net_id 127.0.0.1.1.1`

To see an example of a parameter passed to pytest programmatically, see the use of CMDOPT_OPTION in `pmps_test/pmps/main.py`.

## Documentation

Sphinx-generated documentation for this project can be found here:
https://pcdshub.github.io/pmps_test/


## Requirements

From the main pmps_test directory run the following command to install the requirements:

`pip install -r requirements.txt`

From the main pmps_test directory run the following command to install the development requirements:

`pip install -r dev-requirements.txt`

## Installation

From the main pmps_test directory run the following to install pmps_test in your virtual environment:

`pip install -e .`

## Running the Tests

`python run_tests.py`
   
## Directory Structure

This repo is based the PCDS python cookiecutter. See the following github page for more info:

- `cookiecutter-pcds-python <https://github.com/pcdshub/cookiecutter-pcds-python>`_
