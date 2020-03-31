import logging 

logger = logging.getLogger(__name__)

import argparse
import os
from pathlib import PurePath
import sys
from textwrap import dedent, fill

import pytest

import pmps_test
from ..pmps.conftest import AMS_NET_ID_OPTION
import pmps_test.pmps

DESCRIPTION = fill(dedent("""
    Test suite for PMPS. Unrecognized arguments will be passed directly to
    pytest.
    """)).strip()

def main(args=None):

    top_parser = argparse.ArgumentParser(
        prog="pmps_test",
        description=DESCRIPTION,
    )
    
    top_parser.add_argument(AMS_NET_ID_OPTION, type=str)

    #unknown_args are not recognized by argparse and will be sent to pytest
    args, unknown_args = top_parser.parse_known_args(args)
    print(args)
    print(unknown_args)

    conf_test_file = PurePath(PurePath(pmps_test.pmps.__file__).parent)   

    pytest_args = [
        "--pyargs",
        "pmps_test.pmps",
        "--trace-config",
        f"--confcutdir={conf_test_file}",
        #f"{AMS_NET_ID_OPTION}={args.ams_net_id}"
        #"--cmdopt=2",
    ]
    #] + unknown_args

    pytest_plugins = []

    pytest.main(
        args=pytest_args,
        plugins=pytest_plugins,
    )
    

if __name__ == "__main__":
    main()
