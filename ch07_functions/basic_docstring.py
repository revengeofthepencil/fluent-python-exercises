def factorial(n):
    """ this right here returns n! """
    return 1 if n < 2 else n * factorial(n - 1)

def reverse(word):
    return word[::-1]

def main():
    print("a few demo snippets for functions")
    factorial_res = factorial(12)
    print('factorial_res for 12 %i' % factorial_res)

    print(factorial.__doc__)

    local_fact = factorial
    print('local fact 5 = %i' % local_fact(5))

    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    sorted_by_alpha = sorted(fruits)
    print('sorted_by_alpha = %s' % sorted_by_alpha)

    sorted_by_length = sorted(fruits, key=len)
    print('sorted_by_length = %s' % sorted_by_length)

    sorted_by_reverse = sorted(fruits, key=reverse)
    print('sorted_by_reverse = %s' % sorted_by_reverse)

    # use modern listcomp instead of map
    factor6 = [factorial(n) for n in range(6)]
    print(factor6)

    # use modern generator instead of filter
    event_factors = [factorial(n) for n in range(6) if n % 2] 
    print(event_factors)

if __name__ == "__main__":
    main()
