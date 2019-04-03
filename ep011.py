#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 011 - Loops Part 3: List Comprehension


import calendar
import os


def squares_using_for_loop():
    """
    Print squared numbers using a simple for loop
    """

    squares = []
    for num in range(100):
        # num*num would produce a TypeError
        squares.append(str(num*num))

    print('\n'.join(squares))


def squares_using_list_comprehension():
    """
    Print squared numbers using a list comprehension
    """

    # join method requires string types
    # squares = range(100) would produce a TypeError
    # squares = range(100)
    squares = [str(x*x) for x in range(100)]

    print('\n'.join(squares))


def lc_examples():
    """
    Practical examples of list comprehension
    """

    # print only females

    people = ['1056111', '2034123', '1159323', '2122312', '2131345']
    print('\n'.join([f for f in people if f.startswith('2')]))

    print("==============================")

    # print only directories from the current directory
    print('\n'.join([f for f in os.listdir('.') if os.path.isdir(f)]))

    print("==============================")

    # print only files from the current directory
    print('\n'.join([f for f in os.listdir('.') if os.path.isfile(f)]))

    print("==============================")

    # print only python script files
    print('\n'.join([f for f in os.listdir('.') if f.endswith('.py')]))


def list_leap_years(start=1, stop=10000):
    """
    List only leap years from the given list
    """

    years = range(start, stop)
    # leap_years = [str(year) for year in years if year % 4 == 0 and year % 100 != 0 or year % 400 == 0]

    # a pythonic version
    leap_years = [str(year) for year in years if calendar.isleap(year)]

    print('\n'.join(leap_years))


def main():
    """Entry Point"""

    # squares_using_for_loop()
    # squares_using_list_comprehension()
    # list_leap_years(2019,2119)
    lc_examples()


if __name__ == '__main__':
    main()
