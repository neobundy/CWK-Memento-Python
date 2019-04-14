#!/usr/bin/env python3
# Wankyu Choi - Creative Works of Knowledge 2019
# https://www.youtube.com/wankyuchoi
#
#
# Episode 017 - Data Types: Dictionary Type


def main():
    """Entry Point"""

    print("=" * 10, "Weapon Sound Effects", "=" * 10)

    weapons = {
        'pistol': 'bang',
        'blazer': 'pew',
        'shotgun': 'pow',
        'machine gun': 'rat-a-tat-tat-tat',
        'rocket launcher': 'boom'
    }

    # how does a machine gun go?
    print("A machine gun goes {}!".format(weapons['machine gun']))

    # fetching only keys
    for w in weapons:
        print(w)

    for k, v in weapons.items():
        print(f'Firing a {k.title()}: {v.upper()}!')

    new_weapons = dict(pistol='bang', blazer='pew', machine_gun='rat-a-tat-tat-tat', rocket_launcher='boom')

    for k, v in new_weapons.items():
        print(f"Firing a {k.replace('_', ' ').title()}: {((v.upper() + ' ') * 2).strip()}!!")

    print(new_weapons.keys())
    print(new_weapons.values())

    print("=" * 10, "Word Quiz", "=" * 10)

    japanese_words = {
        'けん': '[剣] - 검',
        'つるぎ': '[剣·劔] - 양날검',
        'かたな': '[刀] - 외날검',
        'やいば': '[刃] - 칼(뽀대 표현)'
    }

    for k, v in japanese_words.items():
        answer = input(f'Guess what {k} means: ')
        print(f'{k} means {v}.')
        print(v.find(answer))
        # if v.find(answer) >= 0:
        if answer in v:
            print('Good job.')
        else:
            print('Nah...')

    print("=" * 10, "Extending Dictionary", "=" * 10)

    japanese_words['ふうせん'] = '[風船] - 풍선'

    print(japanese_words)

    if 'やいば' not in japanese_words:
        japanese_words['やいば'] = '[刃] - 칼(뽀대 표현)'

    print(japanese_words)

    japanese_words['やいば'] = '[刃] - 뽀대있는 표현 칼'

    print(japanese_words)

    delim = ';'
    new_meaning = '긴 칼의 총칭'
    japanese_words['けん'] = japanese_words['けん'] + delim + new_meaning

    print(japanese_words)

    for k, v in japanese_words.items():
        counter = 1
        for m in v.split(delim):
            print(f'{k} means ({counter}) {m}.')
            counter += 1

    print("=" * 10, "Dictionary Methods", "=" * 10)

    # print(japanese_words['いたで'])
    print(japanese_words.get('いたで'))
    print(japanese_words.get('いたで', 'No entry.'))

    word = japanese_words.pop('やいば')
    print(word)
    print(japanese_words)

    del japanese_words['かたな']
    print(japanese_words)

    print("=" * 10, "Merging Dictionaries", "=" * 10)

    new_words = {
            'いたで': '[痛手] - 깊은 상처',
            'きょうりょく': '[強力] - 강력',
            'いちげき': '[一撃] - 일격',
            'むりょく': '[無力] - 무력',
            'やいば': '[刃] - 칼(뽀대 표현)'
    }

    japanese_words.update(new_words)

    print(japanese_words)

    print("=" * 10, "Dictionary Comprehension", "=" * 10)

    new_japanese_words = {k: v.split(delim) for k, v in japanese_words.items()}

    print(new_japanese_words)

    print("=" * 10, "Sorting Dictionary", "=" * 10)

    keys = list(new_japanese_words.keys())
    keys.sort()

    for k in keys:
        print(f'{k} : {new_japanese_words[k]}')


if __name__ == '__main__':
    main()
