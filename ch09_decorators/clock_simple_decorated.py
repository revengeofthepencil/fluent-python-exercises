import time
from clock_simple import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n -1)

def main():
    print('run simple clock')
    snooze(3)

    factorial_result = factorial(6)
    print(f'factorial_result = {factorial_result}')

if __name__ == "__main__":
    main()
