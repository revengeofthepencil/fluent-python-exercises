def main():
    print('merging examples')
    d1 = { 'a': 3, 'b': 4 }
    d2 = { 'c': 5, 'd': 6 }
    merged = d1 | d2
    print(f"merged = {merged}")
    print(f"d1 starts as = {d1}")
    d1 |= d2
    print(f"d1 ends as = {d1}")

    

if __name__ == '__main__':
    main()