def zadanie_1():
    # rozwiązanie zadania 1
    text = input("Podaj dowolne zdanie rozdzielone separatorem\n")
    sep_input = input("Podaj separator, który wystepuje w zdaniu.\n")
    sep_output = input("Podaj separator, na który chcesz zamienić.\n")

    podzielone = text.split(sep_input)
    nowe_zdanie = sep_output.join(podzielone)

    return nowe_zdanie

# treść zadania 4
# Wprowadź z klawiatury dowolny łańcuch znaków i zapisz go do zmiennej. Następnie bazując na przykładzie poniżej zapisz również wyniki dla metod isalpha(), isascii(), isprintable(), istitle(), isupper(). wejscie = input() print(f"Łańcuch {wejscie} isdecimal: {wejscie.isdecimal()}").
# CTRL + / - dodanie/usunięcie komentarza

def zadanie_4():
    inp = input("Wpisz zdanie.\n")
    # f-string - litera 'f' przed łańcuchem powoduje mechanizmu formatowania
    # dla danego łańcucha znaków (zmiennej typu str)
    print(f"Łańcuch {inp} isdecimal: {inp.isdecimal()}")
    print(f"Łańcuch {inp} isalpha: {inp.isalpha()}")
    print(f"Łańcuch {inp} isascii: {inp.isascii()}")
    print(f"Łańcuch {inp} isprintable: {inp.isprintable()}")
    print(f"Łańcuch {inp} istitle: {inp.istitle()}")
    print(f"Łańcuch {inp} isupper: {inp.isupper()}")


def zadanie_5():
    # przykłady - przetestuj
    print('{:>10}'.format('test'))
    print(f'{"test":>10}')
    print(f'{"test":_>10}')
    print(f'{"*":^7}')
    print(f'{"*" * 3:^7}')
    print(f'{"*" * 5:^7}')
    print(f'{3.141592653589793:f}')
    print(f'{3.141592653589793:.4f}')
    print(f'{3.141592653589793:08.4f}')

    # z użyciem pętli
    for num in [1, 123, 2345, 7, 55555]:
        print(f'{num:6d}')

    from datetime import datetime

    # przykład formatowania obiektu daty i czasu
    # każda litera w poniższym formacie oznacza jedną ze składowych daty i czasu
    # patrz tabelka: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    print('{:%Y-%m-%d %H:%M}'.format(datetime.now()))
    print(f'{datetime.now():%Y-%m-%d}')

          



# jeżeli skrypt jest pierwszym skryptem, od którego nastąpiło uruchomienie
# "programu" to zmienna __name__ będzie miała wartość __main__, a to
# oznacza, że część kodu po instrukcji if wykona się tylko wtedy
# __ nazywane są dunder (double underscore)
# modyfikatory dostępu: private, public, protected - brak w Pythonie
if __name__ == '__main__':
    # print(zadanie_1())
    # print(zadanie_4())
    # print('Jestem main!')
    zadanie_5()

# __name__ == '__main__' porównanie
# __name__ = '__main__' przypisanie