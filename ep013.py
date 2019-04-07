#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 012 - Data Types: Numeric Types


import math
from decimal import *
from statistics import mean


def main():
    """Entry Point"""

    # big integers
    print(2 ** 100)
    print(9 ** 1000)
    print(len(str(9 ** 1000)))

    print("======" + "======")

    print("=" * 20)

    # decimal, hexadecimal, octal, binary

    a_decimal = 11
    a_hex = 0x11  # same as 0X11
    an_octal = 0o11  # same as 0O11
    a_binary = 0b11  # same as 0B11

    integers = [a_decimal, a_hex, an_octal, a_binary]

    for i in integers:
        print(i)

    print("=" * 20)

    print(hex(0xF + 1))
    print(oct(0o7 + 1))
    print(bin(0b1 + 1))

    print(0xF + 1)
    print(0o7 + 1)
    print(0b1 + 1)

    print("=" * 20)

    print(hex(256))
    print(oct(256))
    print(bin(256))

    print("=" * 20)

    # int(num_in_str, base)

    print(int('11', 16))
    print(int('11', 8))
    print(int('11', 2))

    print("=" * 20)

    # automatic type casting

    print(7 / 3)
    print(type(7 / 3))

    print(int(7 / 3))
    print(round(7 / 3, 2))

    print(type(float(2)))

    print("=" * 20)

    # using format() method

    numbers = """
11 in hexadecimal: {0:x}
11 in hexadecimal: {0:X}
      11 in octal: {1:o}
     11 in binary: {2:b}
"""

    print(numbers.format(11, 11, 11))

    print("=" * 20)

    # % operator

    print("%.2f" % math.pi)
    print("%.5f" % math.e)

    print("=" * 20)

    # precision issues with binary floats

    print(0.1 + 0.1 + 0.1 - 0.3)
    print(0.1)
    print(1 / 3)

    print(.1 + .1 + .1 == .3)

    print("=" * 20)

    # decimal module

    print(getcontext())
    print(Decimal('1') / Decimal('7'))

    getcontext().prec = 4

    print(Decimal('1') / Decimal('7'))

    print(Decimal('.1') + Decimal('.1') + Decimal('.1') - Decimal('.3'))

    print("=" * 20)

    # some useful built-in functions

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum(nums))
    print(min(nums))
    print(max(nums))
    print(sum(nums) / len(nums))
    print(mean(nums))

    print("=" * 20)

    # math module: dir() returns a list of attributes/methods of an object

    print("\n".join(dir(math)))


if __name__ == '__main__':
    main()
