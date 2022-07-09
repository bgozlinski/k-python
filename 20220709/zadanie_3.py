from time import sleep


def foo(a, b, c):
    return a * b * c


def p(x):
    return f'{x}'


def delay(func, delay_time, *args, **kwargs):
    sleep(delay_time / 1000)
    return func(*args, **kwargs)


assert delay(foo, 1000, 2, 2, 3) == 12
assert delay(p, 1000, 'Ala ma kota') == 'Ala ma kota'


