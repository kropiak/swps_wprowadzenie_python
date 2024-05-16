def zadanie_1():
    # rozwiązanie zadania 1
    text = input("Podaj dowolne zdanie rozdzielone separatorem\n")
    sep_input = input("Podaj separator, który wystepuje w zdaniu.\n")
    sep_output = input("Podaj separator, na który chcesz zamienić.\n")

    podzielone = text.split(sep_input)
    nowe_zdanie = sep_output.join(podzielone)

    return nowe_zdanie


if __name__ == '__main__':
    print(zadanie_1())