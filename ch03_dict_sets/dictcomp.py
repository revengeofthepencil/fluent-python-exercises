def main():
    print("Chapter 3: Dictionaries and Sets - dict comprehensions")
    bourbon_list = [
        ('Four Roses Single Barrel', 50),
        ('Buffalo Trace', 30),
        ('Knob Creek', 35),
        ('Pappy Van Winkle', 999999),
    ]

    brand_price = { brand: price for brand, price in bourbon_list }
    print(f"brand price map = {brand_price}")

    prices_below_100 = {
        price: brand.upper()
            for brand, price in sorted(brand_price.items())
            if price < 100
    }

    print(f"prices below 100 = {prices_below_100}")


if __name__ == "__main__":
    main()
