import time
import functools

def clock(func):
    @functools.wraps(func)
    def clock_decorated(*args, **kwargs):
        time_start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - time_start
        name = func.__name__

        arg_list = [repr(arg) for arg in args]
        arg_list.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_list)
        print(f'[{time_elapsed:0.8f}s] {name}({arg_str}) -> {result}')
        return result
    return clock_decorated