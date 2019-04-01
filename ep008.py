#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 008 - Operators and Conditionals

import math


def list_operators():
    """
    List the examples of python operators

    :return: None
    """

    print("2 + 1 is {}".format(2 + 1))
    print("2 - 1 is {}".format(2 - 1))
    print("2 * 1 is {}".format(2 * 1))
    print("2 / 1 is {}".format(2 / 1))
    print("2 // 1 is {}".format(2 // 1))
    print("3 // 2 is {}".format(3 // 2))
    print("2 % 1 is {}".format(2 % 1))
    print("3 % 2 is {}".format(3 % 2))
    print("2**8 is {}".format(2 ** 8))

    logical_operators = """
    
        Python Logical(Boolean) Operators
    
        >	Greater than: x > y
        <	Less than: x < y
        ==	Equal to: x == y
        !=	Not equal to: x != y
        >=	Greater than or equal to: x >= y
        <=	Less than or equal to: x <= y
    """

    print(logical_operators)

    # Use math module for advanced mathematical calculations
    print("Square root of 2 is {}.".format(math.sqrt(2)))

    print("Operator precedence: 2+2*3 is not {}. It's {}.".format((2+2)*3,2+2*3))


def is_leap_year1(year):
    """
    Is the given year leap year?
    Algorithm 1

    :return: Boolean
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_leap_year2(year):
    """
    Is the given year leap year?
    Algorithm 2

    :return: Boolean
    """

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def check_leap_year():
    """
    Check if the given year is leap year.

    :return: None
    """

    year = 2019

    while year != 0:
        year = int(input("What year is this? Enter 0 to end the program: "))

        if year < 0:
            print("Are you stupid or what?")
            continue
        elif year >= 10000:
            print("Nah...Mankind won't exist that long.")
            continue

        if is_leap_year1(year) and is_leap_year2(year):
            print("Lucky you, in {}, you have 366 days.".format(year))
        else:
            print("You only have 365 days in {}.".format(year))
        print()

    print("Good bye.")


def main():
    """Entry Point"""

    # list_operators()
    check_leap_year()


if __name__ == '__main__':
    main()
