from collections import ChainMap

def main():
    print('chaining example')
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    chain = ChainMap(dict1, dict2)
    print(f'dict1 = {dict1}, dict2 = {dict2}')
    print(f'chain = {chain}')
    # note that it holds the first value
    print(f'chain b = {chain["b"]}')

if __name__ == "__main__":
    main()
