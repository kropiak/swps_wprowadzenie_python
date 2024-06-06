lista = []
lista2 = list()
lista3 = [1, 2, 3]
lista4 = ['a', 5, 'Python', 7.8]

lista3.extend(lista4)
print(lista3)

# # wyjście
# # [1, 2, 3, 'a', 5, 'Python', 7.8]

# # lub w inny sposób
lista6 = lista3 + lista4
print(lista6)

# # lista3.extend(5) # int nie jest iterowalny!
lista3.extend('Ala')
print(lista3)

# # lista3.sort() # sortowanie nie działa, jezeli lista zawiera wartości inne niż liczby

# print(len(lista3))

lista3[:4] = [3, 2, 1]
print(lista3)
print(lista3[100:])
print(type(lista3[100:]))

lista3.insert(6, 7)
print(lista3)

ostatni = lista3.pop()
print(ostatni, lista3)

# rozpakowanie sekwencji (tutaj listy)
order = [1, 2, 3]
first, second, third = order
fourth, *fifth = order

# możemy też rozpakować obiekt typu str
l1, l2, l3 = 'Ala'
print(l1, l2, l3)

# możemy rozpakować krotkę

el1, el2, *reszta = (9, 8, 7, 6, 5, 4, 3)
print(el1, el2)
print(reszta)
print(*reszta)
print(type(reszta))
# print(type(*reszta))


def dodaj(liczba1, liczba2):
    return liczba1 + liczba2


el1, el2, *reszta = (9, 8, 7, 6)

print(dodaj(el1, el2))
print(dodaj(*reszta))  # to tak jak wywołanie dodaj(7,6)

# pakowanie krotki (zmiennych do krotki)
k1 = 9,
print(len(k1))
print(k1)
print(type(k1))

krotka = (1, 2, 'Ala', 'też', 'ma')
# tworzymy krotkę z dwoma elementami (int i lista)
krotka2 = [1, 2, 'Ala', 'też', 'ma'],
krotka3 = tuple([[1, 2, 'Ala', 'też', 'ma']])
# krotka2 = tuple([1, 2, 'Ala', 'też', 'ma'])
print(krotka2)
print(type(krotka2))
# sama krotka nie jest mutowalna, ale lista
# wewnątrz krotki już tak, gdyż to obiekt typu list, który
# jest mutowalny
krotka2[0][3] = 'nie'
krotka3[0][3] = 'nie'
print(krotka2)
print(krotka3)

print(krotka2[2:])
print(type(krotka2[2:]))


# słownik
slownik = dict({'jeden': 1, 'dwa': 2, 'trzy': 3})
# równoważne
slownik = {'jeden': 1, 'dwa': 2, 'trzy': 3}

print(slownik)
print('jeden' in slownik)
print(2 in slownik)  # sprawdzane jest domyślnie przynależenie do kluczy słownika
print(2 in slownik.values()) # tu już szukamy wśród wartości słownika
print(1 in lista4)
print('a' in 'abracadabra')

print(slownik.keys()) # dict_keys(['jeden', 'dwa', 'trzy'])
print(slownik.values()) # dict_values([1, 2, 3])
print(slownik.items()) # dict_items([('jeden', 1), ('dwa', 2), ('trzy', 3)])


for k, v in slownik.items():
    print(f'klucz: {k} to {v}')

for k in slownik:
    print(f'klucz: {k} to {slownik[k]}')


k,v = tuple(slownik.items())[0]
print(k,v)

# # zbiory

czar = set('czabunagunga')
print(czar)
lista = [1,1,1,2,2,2,2,3,3,3,4,4,4,4]
print(list(set(lista)))

# funkcja range

print(range(1, 10))

for i in range(1, 10):
    print(i)

print(list(range(1, 10)))
print(list(range(1, 10, 2)))
print(list(range(10, 2)))
print(list(range(10, 2, -1)))

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

f = frange(0.1, 0.5, 0.1)
print(next(f))  # next() zwraca kolejny element iteratora lub generatora
print('Lalalalala')
print(next(f))



for i in frange(0.1, 0.5, 0.1):
    print(i)


# 1/3 = 0.33333(3)

print((0.1 + 0.2) == 0.3)

print(f'{0.1:.32f}')
print(f'{0.2:.32f}')
print(f'{0.3:.32f}')

from decimal import *

print(round((0.1 + 0.2), 2) == round(0.3, 2))
print((Decimal(0.1) + Decimal(0.2)) == Decimal(0.3))
print((Decimal('0.1') + Decimal('0.2')) == Decimal('0.3'))