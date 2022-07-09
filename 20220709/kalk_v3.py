#  napisz prosty kalkulator, ktory szila tak:
#  jaka operacja? [1-add, 2-sub ...]
# podaj argument a: 10
# podaj argument b: 20
# wynik: 30


def get_opperation():
    opperation = input('Jaka operacje chcesz wykonac? (+, -, *, /)  ')
    if opperation in ['+', '-', '*', '/']:
        return opperation
    return False


def get_numbers():
    a = input("Podaj 1 liczbe: ")
    b = input("Podaj 2 liczbe: ")
    return int(a), int(b)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mutli(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Error: dzielenie przez 0"
    return a / b


def make_opperation(a, b, opperation):
    calc: dict = {"+": add, "-": sub, "*": mutli, "/": div}
    return calc[opperation](a, b)

    # if opperation == '+':
    #     return add(a, b)
    # elif opperation == '-':
    #     return sub(a, b)
    # elif opperation == '*':
    #     return mutli(a, b)
    # elif opperation == '/':
    #     return div(a, b)


def main():
    opperation = get_opperation()
    if opperation:
        a, b = get_numbers()
        foo = make_opperation(a, b, opperation)
        return f'Wynik {a} {opperation} {b} = {foo}'
    return f'Error: Bledna operacja'


if __name__ == '__main__':
    while True:
        print(main())
        q = input("Kontynuowac? [t/n]").lower()
        if q != 't':
            break
