import logging 

logger = logging.getLogger(__name__)

import argparse
import os
from pathlib import PurePath
import sys
from textwrap import dedent, fill

import pytest

import pmps_test


DESCRIPTION = fill(dedent("""
    Test suite for PMPS. Unrecognized arguments will be passed directly to
    pytest.
    """)).strip()

def main(args=None):

    top_parser = argparse.ArgumentParser(
        prog="pmps_test",
        description=DESCRIPTION,
    )
    
    args, unknown_args = top_parser.parse_known_args(args)

    print(args)
    print(unknown_args)

    pytest_args = [
        "--pyargs",
        "pmps_test.pmps",
    ] + unknown_args

    pytest.main(pytest_args)
    

if __name__ == "__main__":
    main()
