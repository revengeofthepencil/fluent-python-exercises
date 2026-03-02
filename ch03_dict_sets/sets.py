def main():
    print('how about somme sets?')
    orig_list = ['hey', 'you', 'guys', 'what', 'you','doing', 'hey', 'wehere', 'you', 'going']
    print(f'orig list = {orig_list}')
    list_to_set = set(orig_list)
    print(f'list to set = {list_to_set}')

    another_list = ['hey', 'dude', 'ok', 'you', 'know']
    print(f'another_list = {another_list}')
    intersect = set(orig_list) & set(another_list)
    print(f'intersect = {intersect}')

    set_from_literal = {1, 2, 3, 4, 1, 2, 3}
    print(f'set from literal = {set_from_literal}')
    pop_set = set_from_literal.pop()
    print(f'popped: {pop_set}, remaining = {set_from_literal}')

    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    common_keys = dict1.keys() & dict2.keys()
    print(f'common keys = {common_keys}')


if __name__ == "__main__":
    main()
