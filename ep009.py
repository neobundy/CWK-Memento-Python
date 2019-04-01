#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 009 - Loops Part 1: while loop

import random


def infinite_loop(infinite=True, max=100):
    """

    An example of an infinite loop.

    :param infinite: let the loop continue infinitely
    :param max: put the break
    :return: None
    """

    num = 0
    while True:
        num += 1
        print("Going...", num)
        if not infinite and (num >= max):
            break


def sum_numbers(is_float=False):
    """
    Sum all numbers given

    :param is_float: if True, use real numbers
    :return: None
    """

    total = 0
    print("Just press enter to end the program.")

    entry = input("Enter your number to add: ")

    while entry:
        if is_float:
            entry = float(entry)
        else:
            entry = int(entry)
        total += entry    # shorthand for total = total + entry
        entry = input("Enter your number to add: ")

    print("The sum of the numbers you've entered: ", total)
    print("Good bye.")


def high_low_game(cheat_mode=False):
    """

    A simple Python implementation of a High-Low number-guessing game

    :param cheat_mode: if True, enable cheat mode
    :return: None
    """

    answer = random.randint(1, 10)

    print("Okay, let's play. I'm thinking of a number between 0 to 10.")
    if cheat_mode:
            print("Cheat mode enabled: {}".format(answer))
    guess = int(input("Take a guess: "))

    max_attempt = 5

    while guess != answer:
        if guess > answer:
            print("Nah... too high.")
        elif guess < answer:
            print("Nope...too low")

        # shorthand for max_attempt = max_attempt - 1
        # Python doesn't allow max_attempt++ nor max_attempt--

        max_attempt -= 1

        if max_attempt == 0:
            print("You lose.")
            print("Better luck next time.")
            break
        elif max_attempt == 1:
            print("You only have 1 try left.")
        else:
            print("You have {} tries left.".format(max_attempt))

        guess = int(input("Take another guess: "))

    else:
        print("Good game.")


def main():
    """Entry Point"""

    # infinite loop
    # infinite_loop()

    # put the break on loop after 100 iterations
    # infinite_loop(False, 100)

    # sum_numbers()
    high_low_game()


if __name__ == '__main__':
    main()
