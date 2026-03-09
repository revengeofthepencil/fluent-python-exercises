from dataclasses import dataclass, field

def main():
    print("check out some data classes")

    @dataclass
    class Party:
        location: str
        time: str
        desc: str = ''
        guests: list[str] = field(default_factory=list)

        def __post_init__(self):
            if (self.desc == '' and self.time.lower() == 'midnight'):
                self.desc = 'Past my bedtime'

    party1 = Party('somewhere', 'noon', 'Lunch!')
    print(f"party 1 = {party1}")
    party1.guests.append('frogs')
    print(f"party 1 after guests = {party1}")

    # Hey! The guests no longer carry over the way they did with named tuples
    party2 = Party('somewhere else', 'midnight')
    print(f"party 2 = {party2}")

    party3 = Party('somewhere else', 'midnight', 'later still', ['me', 'you'])
    print(f"party 3 = {party3}")


if __name__ == "__main__":
    main()
