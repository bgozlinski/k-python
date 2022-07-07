
"""
sałatka:
    pomidor - 350g
    mozarella - 325g
    sałata - 350g
"""
# nazwa, kCal, bialko, tluszcz, weglodowany, cena/kg, waga
pomidor = ["pomidor", 19, 1, 0, 4, 5.7, 350]
mozarella = ["ser mozzarella", 248, 18, 19, 2, 38.32, 325]
salata = ["sałata", 13, 1, 0, 2, 3.15, 350]

lista = [pomidor, mozarella, salata]


def wyliczKalorycznosc(produkt):
    return f'{produkt[0]:20s}, ' \
           f'kalorie: {produkt[1]*produkt[6]/100:>6.2f}, ' \
           f'białko: {produkt[2]*produkt[6]/100:>6.2f}, ' \
           f'tluszcz: {produkt[3]*produkt[6]/100:>6.2f}, ' \
           f'weglowodany: {produkt[4]*produkt[6]/100:>6.2f}, ' \
           f'koszt: {produkt[5]*produkt[6]/1000:>6.2f} zł'


def suma(lista):
    kalorie, bialko, tluszcz, weglowodany, cena, waga = 0, 0, 0, 0, 0, 0
    for i in lista:
        kalorie += i[1]*i[6]/100
        bialko += i[2]*i[6]/100
        tluszcz += i[3]*i[6]/100
        weglowodany += i[4]*i[6]/100
        cena += i[5]*i[6]/1000
    return f'{"SUMA":20s}, ' \
           f'kalorie: {kalorie:>6.2f}, ' \
           f'białko: {bialko:>6.2f}, ' \
           f'tluszcz: {tluszcz:>6.2f}, ' \
           f'weglowodany: {weglowodany:>6.2f}, ' \
           f'koszt: {cena:>6.2f} zł'


def main():
    for i in lista:
        print(wyliczKalorycznosc(i))
    print(f'{"="*len(wyliczKalorycznosc(i))}')
    print(suma(lista))


if __name__ == "__main__":
    main()
