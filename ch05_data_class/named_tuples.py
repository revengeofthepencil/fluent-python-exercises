from collections import namedtuple
from typing import NamedTuple

def main():
    print("check out some named tuples")
    City = namedtuple('City', 'name state country')
    seattle = City('Seattle', 'WA', 'USA')
    print(seattle)
    print('My state is %s' % seattle.state)

    class Coord(NamedTuple):
        lat: float
        long: float
        ref: str = "WGS84"

    seattle_coords = Coord(47.603229, -122.33028)
    print(seattle_coords)

    other_coords = Coord(666, 667, "The neighbor of the beast")
    print(other_coords)

    class Party(NamedTuple):
        location: str
        time: str
        guests: list = []

    party1 = Party('somewhere', 'noon')
    print(f"party 1 = {party1}")
    party1.guests.append('frogs')
    print(f"party 1 after guests = {party1}")

    # gotcha! The guests carry over! Check the dataclass example for default factory
    party2 = Party('somewhere else', 'midnight')
    print(f"party 2 = {party2}")



if __name__ == "__main__":
    main()
