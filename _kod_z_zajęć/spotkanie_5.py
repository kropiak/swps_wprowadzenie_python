if not '':
    print('?')

if '' == False:
    print('Pusty łańcuch to False.')

lista = [1, 3, 5, 7]

if lista:  # not True
    print("Lista nie jest pusta.")

if len(lista) != 0:  # not True
    print("Lista nie jest pusta.")

if not 0:  # not True
    print("int 0")

if not 0.0:  # not True
    print("float 0")


# jak działa pętla for
# ręcznie
r = range(3)

iterator = iter(r)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) # wyjątek StopIteration!

for i in range(3):
    print(i)


# for i in 3: # int nie jest iterowalny
#     print(i)


for index, wartosc in enumerate(lista, start=1):
    print(f'{index} -> {wartosc}')


miesiace = {
    1: 'styczeń',
    2: 'luty', 
    3: 'marzec', 
    4: 'kwiecień', 
    5: 'maj', 
    6: 'czerwiec'
    }

for key, value in miesiace.items():
    print(f'{key} -> {value}')

for item in miesiace.items():
    print(f'{item[0]} -> {item[1]}')
