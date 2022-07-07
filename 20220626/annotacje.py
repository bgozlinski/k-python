def suma(a: int, b: int) -> int:
    """
    Sum of two arguments
    >>> suma(1, 2)
    3

    >>> suma(-1, -2)
    -3

    >>> suma(0, 0)
    0
    """
    return a+b

if __name__ == '__main__':
    import doctest
    doctest.testmod()


# print(suma.__annotations__)
# print(suma.__doc__)

# python -m doctest .\annotacje.py
# python .\annotacje.py -v