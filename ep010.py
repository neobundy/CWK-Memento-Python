#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 010 - Loops Part 2: for loop and iterator


def iterator_example():
    """

    Is range() an iterator?

    :return: None
    """

    iterator_nums = iter([0, 1, 2])
    range_nums = range(0, 3)

    print("Type of iterator_nums: {}".format(type(iterator_nums)))
    print("Type of range_nums: {}".format(type(range_nums)))

    print("You can call next() on an iterator: {}".format(next(iterator_nums)))
    print("You can call next() on an iterator: {}".format(next(iterator_nums)))
    print("You can call next() on an iterator: {}".format(next(iterator_nums)))

    # print("You can call next() on an iterator: {}".format(next(iterator_nums)))

    # this throws an error
    print("You can't call next() on a non-iterator: {}".format(next(range_nums)))


def print_numbers(entry_per_line=5):
    """
    A simple for loop example.

    :param entry_per_line: number of entries to print per line
    :return: None
    """

    # note that 2nd arg for range is exclusive
    for num in range(0, 101):
        if num % entry_per_line == 0:
            print()
        print(num, end=' ')

    for num in range(0, 101, 2):
        if num % entry_per_line == 0:
            print()
        print(num, end=' ')


def game_info():
    """

    A simple for loop example using collection data types.

    :return: None
    """

    # vowels is a tuple
    vowels = ('a', 'e', 'i', 'o', 'u')
    # vowels2 is a set: an unordered collection with unique elements
    # set('aeiou') is the same as
    # vowels2 = {'a', 'e', 'i', 'o', 'u'}
    # vowels2 = set('aeiou')
    # weapons is a list
    weapons = ['blazer', 'chainsaw', 'shotgun', 'assault rifle', 'railgun', 'BFG']
    # player is a dictionary
    player = {'name': 'neobundy',
              'exp': 12700,
              'life': 3,
              'skill_point': 2
              }

    print("Weapon Info({})===========".format(len(weapons)))
    for weapon in weapons:
        # the name of the given weapon starts with a vowel
        if weapon[0] in vowels:
            print("You have an {}.".format(weapon))
        # the name of the given weapon starts with a consonant
        else:
            print("You have a {}.".format(weapon))

    print()

    print("Player Info==========")
    for (key, value) in player.items():
        print(key, ": ", value)


def main():
    """Entry Point"""

    # iterator_example()
    # print_numbers()
    game_info()


if __name__ == '__main__':
    main()
