from clock_improved import clock
import functools

@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n -1) 


@clock
@functools.lru_cache
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n - 2) + fibonacci_cache(n -1) 

def main():
    print('caching example')

    print('first fibonacci run without caching...')
    fibonacci(5)


    print('\nfibonacci run with caching...')
    fibonacci_cache(5)


if __name__ == '__main__':
    main()