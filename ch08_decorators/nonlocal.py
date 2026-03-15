import random

def averager():
    count = 0
    total = 0

    def average(input_val):
        nonlocal count, total
        total += input_val
        count += 1
        return total / count

    return average

def main():
    print('non-local example')
    run_count = 0
    avg = averager()
    while run_count < 10:
        run_count += 1
        current_rand = random.randint(1, 100)
        new_average = avg(current_rand)
        print(f'run {run_count}, current_rand = {current_rand}, new average = {new_average}')


if __name__ == "__main__":
    main()
