def main():
    print("Chapter 2: Sequences - unpacking")
    coords_tuple = (47.6061, -122.3328)
    seattle_lat, seattle_long = coords_tuple
    print(f"Seattle lat = {seattle_lat}, long = {seattle_long}")

    divmod_result = divmod(*coords_tuple)
    print(f"divmod = {divmod_result}")

    # grab excess items
    a, b, *rest = range(1, 7)
    print(f"after range, a = {a}, b = {b}, rest = {rest}")

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    for name, _, _, (lat, lon) in metro_areas:
        # note the formatting - name will be minimum 15 chars
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')




if __name__ == "__main__":
    main()
