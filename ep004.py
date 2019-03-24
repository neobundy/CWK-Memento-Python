#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
# Episode 004 - Pattern Recognition Skill
#

import platform  # importing platform package


def main():
    """Entry Point"""

    if True:
        print("Hello there!")
        print("Good to see ya!")
    else:
        print("What the hell....?")

    my_platform = platform.system()
    my_python = platform.python_version()

    print("You're on {} and have Python Version {}.".format(my_platform, my_python))
    print("운영체제는 {}, 파이썬 버전은 {} 이네요.".format(my_platform, my_python))

if __name__ == '__main__':
    main()
