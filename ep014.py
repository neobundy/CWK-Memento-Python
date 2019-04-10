#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 014 - Data Types: String Type


def main():
    """Entry Point"""

    print("=" * 10, "Class vs. Object Instance", "=" * 10)

    an_int = 10
    a_float = 10.0
    a_string = '10'
    another_string = "10"
    a_raw_string = r'No escaping in \t this raw \n string. C:\Windows\Users\Wankyu Choi'

    yet_another_string = """
    This 
        is
            a
                multiline
                    string.
    """
    yet_yet_another_string = '''
    This 
        is
            another
                multiline
                    string.
    '''

    for obj in [an_int, a_float, a_string, another_string, yet_another_string, yet_yet_another_string, a_raw_string]:
        print(type(obj))
        print(obj)

    print("=" * 10, "Escaping Quotes", "=" * 10)

    single_quote_string = 'I\'ll have a cup of "tea."'
    double_quote_string = "I'll have a cup of \"tea.\""

    print(single_quote_string)
    print(double_quote_string)

    print("=" * 10, "String Indexing and Slicing", "=" * 10)

    filename = "secret.pw"

    print("The first character of the filename: {}".format(filename[0]))
    print("The last character of the filename: {}".format(filename[-1]))

    dot_index = filename.find('.')
    name = filename[:dot_index]
    extension = filename[dot_index + 1:]
    print("Name & extension: {} & {}".format(name, extension))

    print("=" * 10, "String Formatting", "=" * 10)

    print("This is Episode {} ".format(14))
    print("This is Episode {0:>10} ".format(14))
    print("This is Episode {0:04} ".format(14))

    print("You have {:+,} points left.".format(10000))
    print("You have {:+,.3f} points left.".format(-10000))
    print("You have {:x} points left(Hexadecimal).".format(-10000))
    print("You have {:o} points left(Octal).".format(-10000))
    print("You have {:b} points left(Binary).".format(-10000))

    print("=" * 10, "f String", "=" * 10)

    first_name = "Wankyu"
    last_name = "Choi"

    fullname = f'Hi, {first_name:<10} {last_name:>10}!'

    print(fullname)
    print("{first_name} {last_name}".format(first_name="Wankyu", last_name="Choi"))

    points = 30.34
    print(f"You have {points:.3f} points left.")

    print("=" * 10, "Useful String Methods", "=" * 10)

    username = "wankyu choi"

    print("Capitalized username: {}".format(username.capitalize()))
    new_username = username.upper()
    print("Uppercase username: {}".format(username.upper()))
    if new_username.isupper():
        print("Lowercase username: {}".format(new_username.lower()))

    print("Case-swapped username: {}".format(username.capitalize().swapcase()))

    (first_name, last_name) = username.split()
    print("Fullname: {} {}".format(first_name.capitalize(), last_name.capitalize()))

    print(first_name + ' ' + last_name)

    print(username.title())

    s = "This is a string which means nothing."
    print("The string has {} word(s) in it.".format(len(s.split())))

    delimiter = "|"
    s = "This is a string{0} separated by{0} a special delimiter.".format(delimiter)
    print("The string has {} units.".format(len(s.split(delimiter))))

    new_s = "\n".join(s.split(delimiter))
    print(new_s)

    bad_word_list = ['fuck', 'shit', 'ass']

    user_response = "Fuck you, asshole! Shit!"

    print(user_response)

    censored_response = user_response

    for w in bad_word_list:
        censored_response = censored_response.lower().replace(w, "*" * len(w))

    print(censored_response)

    password = "a1234$"

    if password.isnumeric():
        print("No alphabet found.")

    if password.isalpha():
        print("No numeric found.")

    if password.isalnum():
        print("Password must contain at least one special character.")

    password_with_whitespaces = '  dkf3dsl\tkfj1293\t\t    '

    print("[", password_with_whitespaces.strip(), "]")


if __name__ == '__main__':
    main()
