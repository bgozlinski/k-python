from kalk_v3 import make_opperation

#  odczytaj dane z data.txt i wykonaj obliczenie zgodnie z zawartoscia wierszy
#  wiersze zbudowane sa wg schematu
#  operacja a b


with open('data.txt') as f:
    data = f.readlines()

    for line in data:
        operation, a, b = line.split()
        print(f'{a} {operation} {b} = {make_opperation(int(a), int(b), operation)}')
