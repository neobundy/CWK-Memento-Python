#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 012 - Loops Part 4: Generators

import calendar

def irange(*args):
    """
    A range() implementation with the inclusive *stop* argument.
    """

    num_args = len(args)
    start = 1
    stop = 1
    step = 1

    if not num_args:
        raise Exception("At least one argument is required.")
    elif num_args == 1:
        stop = args[0]
    elif num_args == 2:
        (start, stop) = args  # same as start = args[0], stop = args[1]
    elif num_args == 3:
        (start, stop, step) = args
    else:
        raise Exception("Too many arguments: {}".format(num_args))

    for i in range(start, stop+1, step):
        yield i


def main():
    """Entry Point"""

    for i in irange(): print(i)
    # for i in irange(1,10,2,2): print(i)
    # for i in irange(10): print(i)
    # for i in irange(3,20): print(i)
    # for i in irange(1,10,2): print(i)
    # range_obj = range(1,5)
    # print(type(range_obj))
    # generator_obj = irange(1,5)
    # print(type(generator_obj))
    # print(next(generator_obj))
    # print(next(generator_obj))
    # print(next(generator_obj))
    # print(next(generator_obj))

    # years = (year for year in irange(2019, 2019+12) if calendar.isleap(year))
    # print(type(years))
    # print(next(years))
    # print(next(years))
    # print(next(years))
    # print(next(years))
    # print(len(list(years)))
    # years = (year for year in irange(2019, 2019+12) if calendar.isleap(year))
    # next(years)


if __name__ == '__main__':
    main()
