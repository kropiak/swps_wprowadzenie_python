
lista4 = ['a', 5, 'Python', 'Python', 7.8, [1, 2, 3]]

lista4[2]
print(lista4[2:4:1])  # start:stop:step
# print(lista4[2:len(lista4):1])  # start:stop:step
print(lista4[-2::1])  # start:stop:step

lista4.append(10)
print(lista4.index('Python'))
print(lista4.index('Python', 3))

# czy to faktycznie kopia wartości zmiennej lista4 do zmiennej lista5?
lista5 = lista4
lista5.append(0)
print(lista4)
print(lista5)

# sprawdzamy identyfikator obiektu (coś jak adres w pamięci komputera)
print(id(lista4[-1]))
print(id(lista5[-1]))

# tak lepiej, ale zbodnie z opisem metody copy() jest to płytka kopia
lista5 = lista4.copy()

# jeżeli do listy w liście (czyli podlisty [1,2,3]) dodamy element
lista5[-1].append(4)

# to będzie on dodany w kopii również! Bo płytka kopia powoduje skopiowanie tylko
# referencji (odwołania do pamięci) w płytki sposób, bez wykonania tego dla
# każdego elementu zagnieżdżonych kolekcji, a mówiąc bardziej profesjonalnie - bez
# kopiowania wartości dla całego grafu obiektów rozchodzącego się od obiektu lista4, dla
# którego metoda copy() została wywołana
print(lista4)
print(lista5)


print(id(lista4[-1]))
print(id(lista5[-1]))


from copy import deepcopy

# kopia głęboka, wykona kopiowanie dla całego grafu obiektów od obiektu lista4
# warto te fragmenty kodu wrzucic sobie na www.pythontutor.com i zobaczyć
# jak wygląda wizualizacja tego mechanizmu
lista5 = deepcopy(lista4)
print(id(lista4[-1]))
print(id(lista5[-1]))


# wycinki dla list
lista = [[1, 2, 3], ['a', [1, 3], 5, 'Python', 7.8]]
lista[1][1][0] # 1

# wycinek z obiektu str jest obiektem str
print('marmolada'[5:]) # lada

# wycinek z obiektu list jest obiektem list
print(lista[1][2:])
print(lista[1][-3::1])

# dodawanie list to łączenie elementów tych jest w jedną listę (wygodne)
polaczona = lista[0] + lista[1][-3::1]
print(polaczona)
print(lista[0] + lista[1][0:1] + lista[1][1])