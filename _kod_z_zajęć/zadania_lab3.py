# Zadanie 1
# Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5 liczb zostało w oryginalnej liście, a pozostałe 5 znalazło się w nowej liście.

lista = list(range(1, 11))
# gdybysmy chcieli dynamicznie wyznaczyć środek
# dla parzystej liczby elementów w zmiennej lista
# cut = len(lista) // 2
# nowa_lista = lista[cut:]
# lista = lista[:cut]

nowa_lista = lista[5:]
lista = lista[:5]

# można też tak
# for n in range(5):
#     lista.pop()

##########################################################
# zadanie 2
# Połącz te listy ponownie. Dodaj do listy wartość „0” na początku. Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.

merged_lists = lista + nowa_lista
merged_lists.insert(0,0)
merged_lists = [0] + merged_lists

merged_list_copy = merged_lists.copy()
merged_list_copy.sort(reverse=True)


# Zadanie 3
# Napisz skrypt, który pobierze dowolny tekst ze standardowego wejścia poprzez funckję input(). Następnie wyświetl ciąg unikalnych znaków z wczytanego zdania, zapisanych alfabetycznie małymi literami.

# wejscie = input('Wpisz cokolwiek\n')
# unikalne = set(wejscie.lower())
# lista_unikalnych = list(unikalne)
# lista_unikalnych.sort()


# Zadanie 4
# Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) a wartościami nazwy polskich miesięcy.

# miesiace = {1: 'styczeń', 2: 'luty', 3: 'marzec', 4: 'kwiecień', 5: 'maj', 6: 'czerwiec'}

miesiace = {
    1: 'styczeń',
    2: 'luty', 
    3: 'marzec', 
    4: 'kwiecień', 
    5: 'maj', 
    6: 'czerwiec'
    }

# Zadanie 5
# Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy. Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się poprzez wyrażenie: months['pl'][4] a dla wersji angielskiej poprzez months['en'][4].

miesiace_en = {
    1: 'January',
    2: 'February', 
    3: 'March', 
    4: 'April', 
    5: 'May', 
    6: 'June'
    }

months = {'pl': miesiace, 'en': miesiace_en}
# równoważne
months['pl'] = miesiace
months['en'] = miesiace_en

months['pl'][4]
months['en'][4]

# Zadanie 6
# Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie miał przypisaną wartość 1. Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1} Czy można w funkcji fromkeys() użyć dynamicznie podawanej wartości dla każdego klucza słownika?

imie = 'Marianna'

print(dict().fromkeys(imie, 1))


# Zadanie 7
# Wykorzystaj moduł string i następnie:

# wczytaj ze standardowego wejścia dowolny łańcuch znaków,
# używając formatowania łańcuchów (f-string) wyświetl ile znaków oraz jaki % tych znaków (zamienionych na małe litery) z wprowadzonego tekstu pokrywa się ze znakami zapisanymi w zmiennych: string.ascii_lowercase oraz string.digits

import string

wejscie = input('Wpisz coś\n').lower()

wejscie_set = set(wejscie)
ascii_lowercase_set = set(string.ascii_lowercase)

przeciecie = len(wejscie_set.intersection(ascii_lowercase_set))

print(f'We wprowadzonym zdaniu jest {przeciecie} znaków ze zbioru string.ascii_lowercase.')
print(f'Co stanowi {przeciecie / len(string.ascii_lowercase) * 100:.2f}% elementów zbioru string.ascii_lowercase.')


print()