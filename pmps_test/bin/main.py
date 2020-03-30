import logging 

logger = logging.getLogger(__name__)

import os
from pathlib import PurePath

import pytest

import pmps_test

def main():
    pytest.main([
        "--pyargs",
        "pmps_test.pmps",
        #"-vrxs",
    ])
    print("Main has run")


if __name__ == "__main__":
    main()
