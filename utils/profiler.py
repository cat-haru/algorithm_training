def time_performance(f):
    import time
    from functools import wraps

    @wraps(f)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = f(*args, **kwargs)
        t2 = time.time()
        print(f'@profiler: {f.__name__}() took {t2 - t1} seconds.')

        return result
    return measure_time