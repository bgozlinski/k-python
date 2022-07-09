"""
sałatka:
    pomidor - 350g
    mozarella - 325g
    sałata - 350g
"""
#  nazwa, kCal, bialko, tluszcz, weglodowany, cena/kg, waga
lista = [
    ["pomidor", 19, 1, 0, 4, 5.7, 350],
    ["ser mozzarella", 248, 18, 19, 2, 38.32, 325],
    ["sałata", 13, 1, 0, 2, 3.15, 350],
]


def wylicz_kalorycznosc(produkt):
    output = (
        f"{produkt[0]:20s}, "
        f"kalorie: {produkt[1] * produkt[6] / 100:>6.2f}, "
        f"białko: {produkt[2] * produkt[6] / 100:>6.2f}, "
        f"tluszcz: {produkt[3] * produkt[6] / 100:>6.2f}, "
        f"weglowodany: {produkt[4] * produkt[6] / 100:>6.2f}, "
        f"koszt: {produkt[5] * produkt[6] / 1000:>6.2f} zł"
    )
    return output


def suma(lista_produktow: list) -> str:
    kalorie, bialko, tluszcz, weglowodany, cena, waga = 0, 0, 0, 0, 0, 0
    for i in lista_produktow:
        kalorie += i[1] * i[6] / 100
        bialko += i[2] * i[6] / 100
        tluszcz += i[3] * i[6] / 100
        weglowodany += i[4] * i[6] / 100
        cena += i[5] * i[6] / 1000

    output = (
        f'{"SUMA":20s}, '
        f"kalorie: {kalorie:>6.2f}, białko: {bialko:>6.2f}, "
        f"tluszcz: {tluszcz:>6.2f}, weglowodany: {weglowodany:>6.2f}, "
        f"koszt: {cena:>6.2f} zł"
    )

    return output


def main():
    for produkty in lista:
        print(wylicz_kalorycznosc(produkty))
    print(f'{"="*len(wylicz_kalorycznosc(produkty))}')
    print(suma(lista))


if __name__ == "__main__":
    main()
