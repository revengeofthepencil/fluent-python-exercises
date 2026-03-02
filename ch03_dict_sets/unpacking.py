def dump(**arg_list):
    return arg_list

def main():
    print('unpacking demo')
    dumped = dump(**{ 'x': 1 }, y = 2, **{ 'z': 3 })
    print(f"dumped = {dumped}")

    # note that 'a' is over-written
    dict_with_unpack = {
        'a': 0,
        'b': 6,
        **{
            'a': 12,
            'c': 99,
            'd': 20
        }
    }
    print(f"dict_with_unpack = {dict_with_unpack}")


if __name__ == "__main__":
    main()
