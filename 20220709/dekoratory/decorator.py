from functools import wraps

show = 1


def decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Przed funkcja")
        if show:

            return func(*args, **kwargs)

        return "Funkcja nie jest wykonana"
        print("Po funkcji")

    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    # wrapper.__annotations__ = func.__annotations__
    return wrapper


@decor
def foo():
    print("foo")


@decor
def bar():
    print("bar")


print(foo())
