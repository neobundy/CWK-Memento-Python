#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
# Episode 006 - Function Signature
#


def add_procedure(x, y):
    """
    add_procedure(x,y)

    Add and print.
    x:   first argument
    y:   second argument
    """

    print(x+y)


def add_function(x=1, y=1):
    """
    add_function(x=1,y=1)

    Add and print.
    x:   first argument
    y:   second argument

    Returns the sum of x and y.
    """

    return x+y


def main():
    """Entry Point"""

    print("Calling a procedure...")
    add_procedure(1,1)

    print()

    print("Calling a function...")
    print(add_function())
    print(add_function(2,5)*3)


if __name__ == '__main__':
    main()
