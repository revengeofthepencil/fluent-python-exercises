def greet(name, greeting="Hello", suffix="!"):
    return f"{greeting}, {name}{suffix}"

def main():
    print('testing optional args')
    greeting1 = greet('Alex', 'Howdy', '?')
    print(greeting1)

    greeting2 = greet('Alex', suffix='&*^(&*^*(^&*))')
    print(greeting2)

if __name__ == "__main__":
    main()
