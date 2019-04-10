#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 015 - Data Types: Boolean Type


def main():
    """Entry Point"""

    print("=" * 10, "Boolean Type", "=" * 10)

    t = True
    f = False

    if t:
        print("Type of t is {}.".format(type(t)))

    if not f:
        print("Type of ff is {}.".format(type(f)))

    tt = 1
    ff = 0

    if tt:
        print("Type of tt is {}.".format(type(tt)))

    if not ff:
        print("Type of ff is {}.".format(type(ff)))

    x = 5
    y = 7
    t_or_f = x > y

    print(type(t_or_f))

    if t_or_f:
        print("{0} is greater than {1}.".format(x, y))
    else:
        print("{1} is greater than {0}.".format(x, y))

    n = None

    if n:
        print("There's something.".format(type(n)))
    else:
        print("There's nothing: {}".format(type(n)))

    username = ''

    if not username:
        print("Please enter your username.")

    ssn = '1056333'

    if ssn.startswith('1'):
        print("Good morning, Sir.")
    else:
        print("Good morning, Ma'am.")

    # ternary expression: a_or_b = a if x else b
    sex = 'Male' if ssn.startswith('1') else 'Female'

    print(sex)
    if sex == 'Male':
        print("Good morning, Sir.")
    else:
        print("Good morning, Ma'am.")


if __name__ == '__main__':
    main()
