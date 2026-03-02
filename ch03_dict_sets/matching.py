def filter_whiskey(bottle: dict) -> str:
    print(f"in filter_whiskey with bottle {bottle}")
    match bottle:
        case { 
            'type': type,
            'price': price,
            'brand': brand
            } if (
                price < 100
                and type.lower() in ['scotch', 'bourbon']
               ):
            return brand
        case _:
            return None

def main():
    print('match')
    bottles = [
        {'brand': 'Westland', 'price': 60, 'type': 'American Single Malt'},
        {'brand': 'Buffalo Trace', 'price': 30, 'type': 'Bourbon'},
        {'brand': 'Arran', 'price': 65, 'type': 'Scotch'},
        {'brand': 'Macallan', 'price': 110, 'type': 'Scotch'},
    ]

    brands = brands = [
        brand for bottle in bottles
            if (brand := filter_whiskey(bottle)) is not None
    ]
    print(f"Passing brands = {brands}")


if __name__ == '__main__':
    main()