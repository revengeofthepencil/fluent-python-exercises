def number_string(number_input):
    return f"The number is {number_input}. Double it for {number_input * 2}"

def main():
    print("Chapter 2: Sequences - list comprehension and generators")
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

    numbers  = range(1, 11)
    num_strings = [last := number_string(num) for num in numbers]
    print(num_strings)
    print(f"Last one is {last}")

    # listcomp with filter
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)

    # cartesian products
    colors = ['red', 'yellow', 'blue']
    sizes = ['small', 'med', 'large', 'XL']
    all_colors_sizes = [(color, size) for color in colors
                for size in sizes]
    print(all_colors_sizes)

    # try it with a generator. Note the use of parenthesis instead of brackets. 
    # saves memory because it yields items one
    sym_tuple = tuple(ord(symbol) for symbol in symbols)
    print(sym_tuple)

    for tshirt in (f'{c} {s}' for c in colors for s in sizes):
        print(tshirt)

if __name__ == "__main__":
    main()
