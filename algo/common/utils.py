from typing import Callable


class TimeProfiler:
    def __init__(self, is_nano=False):
        self.is_nano = is_nano
        pass

    def __call__(self, f: Callable) -> Callable:
        from time import time, time_ns
        from functools import wraps

        @wraps(f)
        def measure_time(*args, **kwargs):
            start = time_ns() if self.is_nano else time()
            result = f(*args, **kwargs)
            end = time_ns() if self.is_nano else time()

            tdelta = end - start if self.is_nano else '{:9f}'.format(end - start)
            print(f"{f.__name__}() took {tdelta} {'nano ' if self.is_nano else ''}seconds")

            return result

        return measure_time


def memo(f):
    mem = {}

    def wrapper(*args):
        if args not in mem:
            print(f'[{f.__name__}] first compute for {args}')
            mem[args] = f(*args)
        else:
            print(f'[{f.__name__}] there is memo for this args : {mem[args]}')
        return mem[args]
    return wrapper


def paging_content(content, pindex, psize):
    pindex = pindex - 1

    if len(contents) < pspttize:
        pages = [contents]
    else:
        pages = [contents[i:i+psize] for i in range(0, len(contents), psize)]

    if pindex >= len(pages):
        return list()

    return pages[pindex]
