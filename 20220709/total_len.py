

def total_length(*args):
    i = 0
    for j in args:
        i += len(j)
    return i


def total_length2(*iterables):
    i = 0
    for iterable in iterables:
        for _ in iterable:
            i += 1
    return i


def total_length3(*args):
    return sum(
        1
        for iterable in args
        for _ in iterable
    )



assert total_length3([4, 5], (6, 7)) == 4
assert total_length3(range(10), range(10)) == 20
assert total_length3('hello', {'red': 50, 'purple': 100}) == 7
numbers = [4, 6, 8, 9]
assert total_length3(n for n in numbers if n % 2 == 0) == 3
assert total_length3(enumerate(numbers), (n**2 for n in numbers)) == 8

total_length(range(1000), range(1000000000))







