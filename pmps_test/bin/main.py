import argparse
import logging
from pathlib import PurePath
from textwrap import dedent, fill

import pytest

import pmps_test
from ..pmps.conftest import AMS_NET_ID_OPTION
import pmps_test.pmps

logger = logging.getLogger(__name__)


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

    # unknown_args are not recognized by argparse and will be sent to pytest
    args, unknown_args = top_parser.parse_known_args(args)
    print(args)
    print(unknown_args)

    pmps_test_root_dir = PurePath(PurePath(pmps_test.pmps.__file__).parent)

    pytest_args = [
        #"-p",
        #"pmps_test_pmps",
        #"--pyargs",
        f"{pmps_test_root_dir}",
        "--cmdopt=90",
    ] + unknown_args
    pytest_plugins = None

    pytest.main(
        args=pytest_args,
        plugins=pytest_plugins,
    )


if __name__ == "__main__":
    main()
