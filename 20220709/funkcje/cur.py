def cut(lista, start, stop):
    l = []
    add = False
    for i in lista:
        print(f'{i} start:{start(i)} stop:{stop(i)}')
        if start(i):
            add = True
            l.append(i)
            print(add)
            if stop(i) and add:
                return l




print(cut([1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x == 7))
print(cut([1, 2, 3, 4, 5, 6, 7, 8], start=lambda x: x > 3, stop=lambda x: x < 7))
cut(["x", "y", "z", "zz"], start=lambda x: x == "y", stop=lambda x: x == "zz")


