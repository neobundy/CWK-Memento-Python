#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi

import platform  # importing platform package


def zen_of_python():
    """Print the Zen of Python"""

    import this # print the zen of python


def main():
    """Entry Point"""

    if True:
        print("Hello there!")
        print("Good to see ya!")

    print("You're on {}.".format(platform.system()))
    print("You have Python Version {}.".format(platform.python_version()))


if __name__ == '__main__':
    main()
