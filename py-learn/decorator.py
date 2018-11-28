from functools import wraps

def tracer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("%s(%r, %r)->%r" % (func.__name__, args, kwargs, result))
        return result
    return wrapper


@tracer
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    fibonacci(3)
    print(fibonacci)
    print('help:')
    help(fibonacci)
