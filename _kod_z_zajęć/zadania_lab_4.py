liczby_podzielne_przez_5 = []

for i in range(51): # ile iteracji? 50
    if i % 5 == 0:
        liczby_podzielne_przez_5.append(i)

print(liczby_podzielne_przez_5)

liczby_podzielne_przez_5 = []

for i in range(0, 51, 5): # ile iteracji? 10
    if i % 5 == 0:
        liczby_podzielne_przez_5.append(i)

print(liczby_podzielne_przez_5)

# można tak
list(range(0, 51, 5))

# Zadanie 2
# Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9, ale tylko nieparzysta wysokość.
#  o 
# ooo
#  o

# 1. wczytujemy wysokosc od uzytkownika
wys = input('Podaj wysokość (3,5,7 lub 9)\n')
if wys.isdigit():
    wys = int(wys)
# 2. sprawdzamy czy wysokosc jest poprawna
if wys % 2 == 1 and wys in [3,5,7,9]:
    # 3. rysujemy diament o zadanej wysokości
    for i in range(1, wys + 1, 2):
        print(f'{"o" * i:^{wys}}')

