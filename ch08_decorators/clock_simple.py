import time

def clock(func):
    def clock_decorated(*args):
        time_start = time.perf_counter()
        result = func(*args)
        time_elapsed = time.perf_counter() - time_start
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{time_elapsed:0.8f}s] {name}({arg_str}) -> {result}')
        return result
    return clock_decorated