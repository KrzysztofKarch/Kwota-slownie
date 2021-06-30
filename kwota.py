# Program do zamiany liczby zapisanej za pomocą cyfr z zakresu
# całkowitego [0 - 999999] na liczbę zapisaną słownie
#
#
# OPIS
# Liczby składają się z rzędów jedności, dziesiątek i setek. Rząd tysiąca (lub dziesiątek tysięcy) traktujemy jak
# powtórzony rząd jedności (lub dziesiątek), z dodanym słowem "tysiąc" w odpowiedniej odmianie gramatycznej.
# Liczbę zapisaną słownie budujemy za pomocą 3 funkcji bazowych, pobrana liczba jest sprawdzana
# i w zależności od jej długości wywołujemy odpowiednie kolejności 3 funkcji bazowych.
#
#
# FUNKCJE BAZOWE:
# Funkcja odczytaj_jednosci() powinna otrzymać tylko 1 znak odpowiadający rzędowi jedności
# Fukcja odczytaj_dziesiatki() powinna otrzymać 2 znaki odpowiadające rzędowi dziesiątek i rzędowi jedności
#     w zależności od wartości otrzymanej liczby wybiera 1 z 4 możliwości:
#     - dla liczb 0,1,2,3,4,5,6,7,8,9 -> slownik_jednosci
#     - dla liczb 11,12,13,14,15,16,17,18,19 -> slownik_kilkanascie
#     - dla liczb 10,20,30,40,50,60,70,80,90 -> slownik_dziesiatki
#     - dla liczb 21-29,31-39,41-49,... -> slownik_dziesiatki + slownik_jednosci
# Funkja odczytaj_setki() powinna otrzymać 1 znak odpowiadający rzędowi setek
#
#
# PRZYKŁADOWY PRZEBIEG programu dla liczby 345111:
# 1. Pobranie liczby
# 2. Sprawdzenie liczby
#     - usunięcie wszystkich znaków białych
#     - sprawdzenie czy użytkownik podał liczbę całkowitą
#     - sprawdzenie poprawności zakresu [0 - 999999]
# 3. Sprawdzenie długości liczby
# 4. Dla liczby 6 cyfrowej, 345111:
#     - dla 1. znaku odczytaj_setki()
#     - dla 2. i 3. znaku odczytaj_dziesiatki()
#         - wartość 45 czyli slownik_dziesiatki(4) + slownik_jednosci(5)
#     - dodaj slowo_tysiac()
#     - dla 4. znaku odczytaj_setki()
#     - dla 5. i 6. znaku odczytaj_dziesiatki
#         - wartość 11 czyli slownik_kilkanascie(11)
#     - dodaj slowo_zlotych()

# #######################################
# Słowniki zawierają słowa kolejnych rzędów liczb
def slownik_jednosci(x):
    a={ '0': 'zero ',
        '1': 'jeden ',
        '2': 'dwa ',
        '3': 'trzy ',
        '4': 'cztery ',
        '5': 'pięć ',
        '6': 'sześć ',
        '7': 'siedem ',
        '8': 'osiem ',
        '9': 'dziewięć '}
    return a[x]

def slownik_kilkanascie(x):
    a={ '11': 'jedenaście ',
        '12': 'dwanaście ',
        '13': 'trzynaście ',
        '14': 'czternaście ',
        '15': 'piętnaście ',
        '16': 'szesnaście ',
        '17': 'siedemnaście ',
        '18': 'osiemnaście ',
        '19': 'dziewiętnaście '}
    return a[x]

def slownik_dziesiatek(x):
    a={ '1': 'dziesięć ',
        '2': 'dwadzieścia ',
        '3': 'trzydzieści ',
        '4': 'czterdzieści ',
        '5': 'pięćdziesiąt ',
        '6': 'sześćdziesiąt ',
        '7': 'siedemdziesiąt ',
        '8': 'osiemdziesiąt ',
        '9': 'dziewięćdziesiąt '}
    return a[x]

def slownik_setek(x):
    a={ '0': '',
        '1': 'sto ',
        '2': 'dwieście ',
        '3': 'trzysta ',
        '4': 'czterysta ',
        '5': 'pięćset ',
        '6': 'sześćset ',
        '7': 'siedemset ',
        '8': 'osiemset ',
        '9': 'dziewięćset '}
    return a[x]

# #######################################
# Funkcja dbająca o poprawną końcówkę słowa "złote"
def slowo_zlotych(x):
    if int(x) < 10:
        zlote = {'0': 'złotych',
                '1': 'złoty',
                '2': 'złote',
                '3': 'złote',
                '4': 'złote',
                '5': 'złotych',
                '6': 'złotych',
                '7': 'złotych',
                '8': 'złotych',
                '9': 'złotych'}
        return zlote[x[-1]]
    elif 10 <= int(x) < 20:
        return 'złotych'
    elif int(x)>= 20:
        zlotych = {'0': 'złotych',
                '1': 'złotych',
                '2': 'złote',
                '3': 'złote',
                '4': 'złote',
                '5': 'złotych',
                '6': 'złotych',
                '7': 'złotych',
                '8': 'złotych',
                '9': 'złotych'}
        return zlotych[x[-1]]

# #######################################
# Funkcja dbająca o poprawną końcówkę słowa "tysiąc"
def slowo_tysiecy(x):
    if int(x) < 10:
        tysiac = {'0': 'tysięcy ',
                '1': 'tysiąc ',
                '2': 'tysiące ',
                '3': 'tysiące ',
                '4': 'tysiące ',
                '5': 'tysięcy ',
                '6': 'tysięcy ',
                '7': 'tysięcy ',
                '8': 'tysięcy ',
                '9': 'tysięcy '}
        return tysiac[x[-1]]
    elif 10 <= int(x) < 20:
        return 'tysięcy '
    elif int(x) >= 20:
        tysiac = {'0': 'tysięcy ',
                '1': 'tysięcy ',
                '2': 'tysiące ',
                '3': 'tysiące ',
                '4': 'tysiące ',
                '5': 'tysięcy ',
                '6': 'tysięcy ',
                '7': 'tysięcy ',
                '8': 'tysięcy ',
                '9': 'tysięcy '}
        return tysiac[x[-1]]
# #######################################
# Funcje bazowe
def odczytaj_jednosci(x):
    """
    powinna otrzymać tylko 1 cyfrę odpowiadającą pozycji jedności,
    przesyła ją do słownika i zwraca odpowiednie slowo
    """
    return slownik_jednosci(x)

def odczytaj_dziesiatki(x):
    """ powinna otrzymać 2 znaki odpowiadający pozycji dziesiątek i jedności,
        przesyła 1 lub 2 do odpowiedniego słownika i zwraca odpowiednie slowo """
    if int(x) == 0:
        slowo = ''
    elif int(x) < 10:
        slowo=slownik_jednosci(x[1])
    elif int(x) > 10 and int(x) < 20:
        slowo=slownik_kilkanascie(x)
    elif int(x) % 10 == 0:
        slowo=slownik_dziesiatek(x[0])
    else:
        slowo=slownik_dziesiatek(x[0])
        slowo+=slownik_jednosci(x[1])
    return slowo

def odczytaj_setki(x):
    """ powinna otrzymać tylko 1 znak odpowiadający pozycji setek,
        przesyła go do słownika i zwraca odpowiednie slowo """
    slowo=slownik_setek(x)
    return slowo

# #######################################
# Pobierz i sprawdź
def pobierz_liczbe():
    liczba=''
    while not liczba:
        liczba = input('Podaj liczbę:')
    return liczba

def sprawdz_liczbe(x):
    x = x.strip()
    try:
        int(x)
        if int(x) < 0 or int(x) > 999999:
            raise ValueError
        else:
            return x
    except ValueError:
        print('liczba nieprawidłowa, konieczna wartość typu "intiger" z zakresu 0 - 999 999', end = '')
        return None

# #######################################
# main
def main():
    while True:
        liczba=pobierz_liczbe()
        liczba=sprawdz_liczbe(liczba)

        slowo=''

        if liczba:
            dlugosc = len(liczba)
            if dlugosc == 1:
                slowo += odczytaj_jednosci(liczba)
            elif dlugosc == 2:
                slowo += odczytaj_dziesiatki(liczba)
            elif dlugosc == 3:
                slowo += odczytaj_setki(liczba[0])
                slowo += odczytaj_dziesiatki(liczba[1:])
            elif dlugosc == 4:
                slowo += odczytaj_jednosci(liczba[0])
                slowo += slowo_tysiecy(liczba[0])
                slowo += odczytaj_setki(liczba[1])
                slowo += odczytaj_dziesiatki(liczba[2:])
            elif dlugosc == 5:
                slowo += odczytaj_dziesiatki(liczba[0:2])
                slowo += slowo_tysiecy(liczba[0:2])
                slowo += odczytaj_setki(liczba[2])
                slowo += odczytaj_dziesiatki(liczba[3:])
            elif dlugosc == 6:
                slowo += odczytaj_setki(liczba[0])
                slowo += odczytaj_dziesiatki(liczba[1:3])
                slowo += slowo_tysiecy(liczba[0:3])
                slowo += odczytaj_setki(liczba[3])
                slowo += odczytaj_dziesiatki(liczba[4:])

            # dodaj końcówkę 'złotych' w odpowiedniej formie
            slowo += slowo_zlotych(liczba)

        print(slowo)

main()
