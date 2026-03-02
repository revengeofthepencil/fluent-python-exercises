from collections import Counter

def main():
    print('counter example')
    ct = Counter('Can you dig it?')
    print(f'count result = {ct}')

    ct.update('I can most certainly dig it')
    print(f'updated count result = {ct}')

    most_common = ct.most_common(3)
    print(f'The 3 most common are {most_common}')

if __name__ == "__main__":
    main()
