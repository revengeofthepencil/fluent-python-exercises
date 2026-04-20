from random import randint
from sentence import Sentence

def dice():
    return randint(1, 6)

def gen_123():
    yield 1
    print('dude! about to print the second one')
    yield 2
    yield 3

def main():
    print("iterator examples")

    print("roll until you get a 3")
    until3 = iter(dice, 3)
    for roll in until3:
        print(roll)

    words = "You're innocent when you dream"
    print(f"try it out with '{words}'")

    my_sent = Sentence(words)
    print(my_sent)

    for word in my_sent:
        print(word)

    g123 = gen_123()
    print(f'g123 = {g123}')
    print(next(g123))
    print(next(g123))
    print(next(g123))

    g123Again = gen_123()
    for num in g123Again:
        print(f"g123Again: {num}")


if __name__ == "__main__":
    main()
