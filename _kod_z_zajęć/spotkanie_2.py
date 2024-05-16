# spotkanie 2
# 1. typ str
# ind   012345678
imie = 'Krzysztof'

print(imie[0])
# imie[0] = 'k' - błąd! TypeError

# dunder (double uderscore __)


zmienna_str = 'dgfjksdgf s fhsdkh fksdhf khk fhksdfh kshdfk hsdkfh kshf khsfk hskdfh kshdfjk hsdkf hkshdf khsfdk hskdfh kshdfk hskdfh kshdfk hksdhf khsfk hkshf hsk hshf khskdfh kshd khsk hksd'

inna_zmienna_str = """Ala ma kota,
 a kot ma Alę."""

# print(inna_zmienna_str)
lista_string = str(list[1,2,3])

print(lista_string)
sentence = input('Wpisz dowolne zdanie:\n')

print('Wpisałeś ' + sentence)
sentence = sentence.capitalize()
# print(sentence.capitalize())
print(sentence)
print(f"Liczba znaków: {len(sentence)}")
print(sentence.count('a'))
# case sensitive - wielkość znaków ma znaczenie (jak w Linuxie)
sentence = sentence.strip()
print(sentence)
print(f"Liczba znaków: {len(sentence)}")
print(sentence.split(','))

print('Ala ma kota\t', 'A kot ma Alę\n', 'Kot lubi myszy', 4, [3, 4])

sentence.isdigit()
print('Ala ma 3 koty'.isdigit())
print('3543535345'.isdigit())

print('3.14'.isdigit())
print('3.14'.isnumeric())
print('3.14'.replace('.','',1).isdigit())

print('3.14'.zfill(8))
print('4'.zfill(8))
print('48785'.zfill(8))

text = 'aBrAcAdAbRa'
print(text[0])
print(text[2])

print(text[0:]) # domyślnie stop to koniec sekwencji*, step=1
print(text[2:]) 
print(text[2::2]) 
print(text[-1::-1]) 
print(text[::-1]) # [-1, -2, -3, -4, -5, ...]
print(text[::-3]) 
print(text[-2::]) # [-2, -1]

print(text[0:2]) # start - inclusive, stop - exclusive (wyłączając wartość stop)

# [ 
 # [1, 2, 3] # [0][2] = 3
 # [4, 5, 6] # [1][1] = 5
 # [7, 8, 9] # [2][0] = 7
# ]
# [wiersze, kolumny]
# [1: , 1:]
# slice dla macierzy (tylko przykład, w praktyce można używać dla tablic numpy oraz pandas)
# lub [1:3, 1:3]


lista = [1, 2, 3, 4, 5, 6]
podzial = len(lista) // 2

print(lista[:podzial]) # indeksy 0,1,2
print(lista[podzial:]) # indeksy 3,4,5

# formatowanie łancuchów znaków

wiek = 10

print('Ala ma {0} lat(a).'.format(wiek))
# print('Ala ma ' + wiek +  ' lat(a).') # błąd!
print(f'Ala ma {wiek} lat(a).') # f-string

print('{0:>10}'.format('test'))
print(f'{".":>10}') # wyrównanie do prawej na 10 pozycjach
print(f'{".":^10}') # wyrównanie do środka ...
print(f'{".":<10}') # wyrównanie do lewej ...


print('{:.5}'.format('długi tekst'))
pi = 3.14159
w_nowym_formacie = f'{pi:06.2f}'
print(w_nowym_formacie)


print('elo\r', end='')
print('zero\r', end='')

print(r'\sciezka\rok\numer\task')
print('\\sciezka\\rok\\numer\\task')

print("\u2764") # string unicode w formie skróconej 16 bit
print("\u2765")
print("\U0001F602") # string unicode 32 bit
