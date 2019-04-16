#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 019 - File

from datetime import date
import pickle
import re


def copy_text_file(source, dest):
    """
    Copy A Text File

    :param source: source file
    :param dest: destination file
    :return: None
    """

    # r: read mode
    # w: write mode
    # a: append mode
    infile = open(source, "rt")
    outfile = open(dest, "wt")
    # outfile = open(dest, "at")

    for l in infile:
        # print(l.rstrip(), file=outfile)
        # print(l, end='', file=outfile)
        outfile.write(l)

    outfile.close()
    print(f'{source} copied to {dest}.')


def copy_binary_file(source, dest, buffer_size=10400):
    """
    Copy A Binary File

    :param source: source file
    :param dest: destination file
    :param buffer_size: size of the buffer
    :return: None
    """

    infile = open(source, "rb")
    outfile = open(dest, "wb")

    buf = infile.read(buffer_size)

    while buf:
        outfile.write(buf)
        buf = infile.read(buffer_size)

    outfile.close()

    print(f'{source} copied to {dest}.')


def split_filename(filename):
    """
    Split filename into name and extension parts

    :param name: filename
    :return: name & extension tuple
    """

    dot_index = filename.find('.')
    name = filename[:dot_index]
    extension = filename[dot_index + 1:]

    return name, extension


def write_database(dic, dest):
    """

    Write the given dictionary into the destination file as a pickle

    :param dic: dictionary
    :param dest: destination file
    :return: None
    """

    with open(dest, 'wb') as f:
        pickle.dump(dic, f)


def read_database(source):
    """

    Read a pickled database from the given source

    :param source: source file
    :return: dictionary
    """

    with open(source, 'rb') as f:
        dic = pickle.load(f)

    return dic


def is_korean(word):
    if re.match(r'(^[가-힣]+)', word):
        return True
    else:
        return False


def is_english(word):
    if re.match(r'(^[a-zA-Z]+)', word):
        return True
    else:
        return False


def is_japanese(word):
    if re.match(r'[一-龠あ-んア-ン]+', word):
        return True
    else:
        return False


def main():
    """Entry Point"""

    timestamp = str(date.today())
    copy_suffix = '-' + timestamp + '.backup'

    print("=" * 10, "Text File", "=" * 10)

    source = 'ep019.py'
    name, ext = split_filename(source)
    dest = name + copy_suffix + '.' + ext

    copy_text_file(source, dest)

    print("=" * 10, "Binary File", "=" * 10)
    source = 'dog.jpg'
    name, ext = split_filename(source)
    dest = name + copy_suffix + '.' + ext

    copy_binary_file(source, dest)

    print("=" * 10, "Read Source Word List Text File", "=" * 10)

    source = 'words.md'
    delim = '-'

    entries = [l.strip() for l in open(source, 'rt') if is_japanese(l[0]) and delim in l]

    japanese_dictionary = {}
    for e in entries:
        k, v = e.split(delim)
        japanese_dictionary[k.strip().replace(' ', '')] = v.strip()
        print(f"{k.strip().replace(' ', '')} means {v.strip()}.")

    print("=" * 10, "Write Japanese Dictionary Database", "=" * 10)
    dictionary_file = 'japanese_dictionary.cwkdb'
    print(japanese_dictionary)
    write_database(japanese_dictionary, dictionary_file)

    print("=" * 10, "Read Japanese Dictionary Database", "=" * 10)
    new_dic = read_database(dictionary_file)
    print(new_dic)


if __name__ == '__main__':
    main()
