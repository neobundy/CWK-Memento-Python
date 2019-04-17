#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 020 - Exception Handling

import pickle


def read_database(source):
    """

    Read a pickled database from the given source

    :param source: source file
    :return: dictionary
    """

    with open(source, 'rb') as f:
        dic = pickle.load(f)

    return dic


def get_number():

    number = input("Enter a number: ")
    if not number.isnumeric():
        raise TypeError(f'What are you, stupid? \'{number}\' is not a number.')
    else:
        return number


def main():
    """Entry Point"""

    print("=" * 10, "Catching A File I/O Error", "=" * 10)

    source = 'nosuchfile.cwk'

    try:
        lines = open(source, "rt")
    except FileNotFoundError:
        print(f'{source} not found. Want to create {source}?')
    except IOError:
        print('File I/O Error.')
    except:
        print('Unknown Error.')
    else:
        print(lines)
    finally:
        # TODO: save a temp file
        print('Temp file saved.')

    print("=" * 10, "Catching A KeyError", "=" * 10)

    source = 'japanese_dictionary.cwkdb'
    dic = read_database(source)

    # word = 'もらう[貰う]'
    word = 'もらう'
    try:
        print(dic[word])
    except KeyError:
        print(f'Word not found: {word}.')

    print("=" * 10, "Raising An Exception", "=" * 10)

    try:
        number = get_number()
    except TypeError as e:
        print(f'Error occurred: {e}')
    else:
        print(f'{number} accepted.')


if __name__ == '__main__':
    main()
