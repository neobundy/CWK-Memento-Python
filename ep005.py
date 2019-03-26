#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
# Episode 005 - Batteries Included
#

import platform
import sys
import cwk_utilities.cwk_info
from cwk_utilities import cwk_info
from cwk_utilities.cwk_info import version
from cwk_utilities.cwk_info import version as cv


def list_search_path():
    """List Package Search Path"""

    for p in sys.path:
        print(p)


def main():
    """Entry Point"""

    my_platform = platform.system()
    my_python = platform.python_version()

    list_search_path()

    print()
    print("You're on {} and have Python Version {}.".format(my_platform, my_python))
    print("You have CWK Utilities Package version {}.".format(cwk_utilities.cwk_info.version()))
    print("You have CWK Utilities Package version {}.".format(cwk_info.version()))
    print("You have CWK Utilities Package version {}.".format(version()))
    print("You have CWK Utilities Package version {}.".format(cv()))


if __name__ == '__main__':
    main()
