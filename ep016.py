#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 016 - Data Types: List Type

from statistics import mean


def main():
    """Entry Point"""

    print("=" * 10, "String Sequence vs. List", "=" * 10)

    name_string = 'wankyu'
    name_list = ['w', 'a', 'n', 'k', 'y', 'u']

    print(name_string[0])
    print(name_list[0])

    # strings are immutable: the following would cause an error
    # name_string[0] = 'W'

    # lists are mutable
    name_list[0] = 'W'
    print(name_list)

    print("=" * 10, "Nested list", "=" * 10)
    jumble = ['a', 1, 0.1, [3, 6]]

    print(jumble[3][1])

    print("=" * 10, "Indexing", "=" * 10)

    a_list = [0, 1, 2, 3, 4, 5]

    print(a_list)
    print("The first element: {}.".format(a_list[0]))
    print("The last element: {}.".format(a_list[-1]))
    print("The second element: {}.".format(a_list[1]))
    print("The second to last element: {}.".format(a_list[-2]))

    print("=" * 10, "Slicing", "=" * 10)

    print(a_list)
    print("From second to fourth elements: {}.".format(a_list[1:4]))
    print("From second to last elements: {}.".format(a_list[1:]))
    print("From first to third to last elements: {}.".format(a_list[:-2]))

    print("=" * 10, "Shallow vs. Deep Copy(By Reference vs. By Value", "=" * 10)

    another_list_shallow_copied = a_list
    another_list_deep_copied = a_list[:]

    print("-" * 5, "Before changing an element in the original list...", "-" * 5)
    print(another_list_shallow_copied)
    print(another_list_deep_copied)

    print("-" * 5, "After changing an element in the original list...", "-" * 5)

    a_list[0] = 'messed up'
    print(another_list_shallow_copied)
    print(another_list_deep_copied)

    print("=" * 10, "Traversing", "=" * 10)

    for i in another_list_deep_copied:
        print(i*i)

    print("=" * 10, "List Comprehension", "=" * 10)

    odd_numbers = [x for x in another_list_deep_copied if x % 2]    # x % 2 == 1
    even_numbers = [x for x in another_list_deep_copied if not x % 2]    # x % 2 == 0

    print("Odd numbers in the list: {}".format(odd_numbers))
    print("Even numbers in the list: {}".format(even_numbers))

    print("=" * 10, "List Operations", "=" * 10)

    list_a = [0, 1, 2]
    list_b = [3, 4, 5]

    print("Adding lists {} and {}: {}".format(list_a, list_b, list_a + list_b))
    print("Multiplying a list {} by {}: {}".format(list_a, 3, list_a * 3))

    print("=" * 10, "Useful List Methods", "=" * 10)

    a_list = list(range(6))

    a_list.append(6)
    print(a_list)

    a_list.extend(a_list)
    print(a_list)

    unsorted_names = ['wankyu', 'james', 'brown', 'fred']
    unsorted_names.sort()
    print(unsorted_names)
    unsorted_names.reverse()
    print(unsorted_names)

    # Won't work
    sorted_names = unsorted_names.sort()
    print(sorted_names)

    big_integers = [1123, 5232, 345, 123, 233, 253, 56344354, 67324]
    print("The sum of {0}: {1:,}".format(big_integers, sum(big_integers)))
    print("The mean of {0}: {1:,}".format(big_integers, mean(big_integers)))

    print("After popping the last element {}: {}".format(big_integers.pop(), big_integers))
    print("After popping the second element {}: {}".format(big_integers.pop(1), big_integers))

    # just trash it
    del big_integers[1]

    print(big_integers)

    big_integers.remove(253)

    print(big_integers)

    del big_integers[1:3]

    print(big_integers)

    big_integers.insert(1, 5555)
    print(big_integers)

    names = ['wankyu', 'james', 'brown', 'wankyu', 'fred', 'wankyu']

    print("{} '{}(s)' found.".format(names.count('wankyu'), 'wankyu'))


if __name__ == '__main__':
    main()
