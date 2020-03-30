import os
from pathlib import PurePath

import pytest

import pmps_test

def main():
    base_directory = PurePath(pmps_test.__file__).parent
    print(base_directory)
    target_directory = PurePath(base_directory, 'pmps')
    print(target_directory)
    target_ini = PurePath(target_directory, 'pytest.ini')
    print(target_ini)
    pytest.main([
        f"{target_directory}",
        #f"--rootdir={target_directory}",
        #f"-c", f"{target_ini}",
    ])
    print("Main has run")


if __name__ == "__main__":
    main()
