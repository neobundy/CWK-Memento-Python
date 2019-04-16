#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 018 - Data Types: Tuple & Set Types


def main():
    """Entry Point"""

    print("=" * 10, "Tuple", "=" * 10)

    a_list = ['wankyu', 'james', 'fred', 'tom', 'harry']
    a_tuple = ('wankyu', 'james', 'fred', 'tom', 'harry')

    print(f'a_list is a {type(a_list)}: {a_list}')
    print(f'a_tuple a {type(a_tuple)}: {a_tuple}')

    a_list[0] = 'ben'
    print(f'a_list is a {type(a_list)}: {a_list}')

    # tuples are immutable
    # a_tuple[0] = 'ben'
    # a_tuple.append('ben')
    # print(f'a_tuple a {type(a_tuple)}: {a_tuple}')

    a = ('wankyu')
    b = ('choi')

    print(f'{a} {b}')

    b, a = a, b

    print(f'{a} {b}')

    args = (3,'key',True)

    a, b, c = args

    print(f'args: 1. {a}, 2. {b}, 3. {c}')

    print("=" * 10, "Pseudo Tuple Comprehension", "=" * 10)

    odd_numbers = (x for x in range(10) if x % 2)

    print(tuple(odd_numbers))

    print("=" * 10, "Set", "=" * 10)

    a_set = {'wankyu', 'james', 'fred', 'tom', 'harry'}
    another_set = set('wankyu james fred tom harry')

    print(f'a_set a {type(a_set)}: {a_set}')
    print(f'another_set a {type(another_set)}: {another_set}')
    print(f'another_set sorted: {sorted(another_set)}')

    list_set = set(dir(list))
    tuple_set = set(dir(tuple))

    print(sorted(list_set))
    print(sorted(tuple_set))

    # Union: 합집합 A | B
    print(f'Union: {sorted(list_set | tuple_set)}')
    print('Union:', sorted(list_set.union(tuple_set)))

    # Intersection: 교집합 A & B
    print(f'Intersection: {sorted(list_set & tuple_set)}')
    print('Intersection:', sorted(list_set.intersection(tuple_set)))

    # Difference: 차집합 A - B
    print(f'Difference: {sorted(list_set - tuple_set)}')
    print('Difference:', sorted(list_set.difference(tuple_set)))

    # Complement: 여집합(보집합) (A | B) - A
    print(f'Complement: {sorted((list_set | tuple_set) - list_set)}')

    # Symmetric Difference: 대칭 차집합 (A | B) - (A & B)
    print(f'Symmetric Difference:{sorted(list_set ^ tuple_set)}')
    print(f'Symmetric Difference: {sorted((list_set | tuple_set) - (list_set & tuple_set))}')

    print("=" * 10, "Set Comprehension", "=" * 10)

    odd_numbers = {x for x in range(10) if x % 2}

    print(odd_numbers)


if __name__ == '__main__':
    main()
