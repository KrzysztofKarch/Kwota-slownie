# Program do zamiany liczby zapisanej za pomocą cyfr z zakresu [0 - 999 999 999] 
# na liczbę zapisaną słownie. Pełne nazewnictwo złotych i groszy. 
#
# Autor: Krzysztof Karch 
# Mail:  krzysztof.karch@wp.pl
# Modyfikacja: 07.07.2021
#
# OPIS
# Liczby składają się z rzędów jedności, dziesiątek i setek. Rząd tysiąca (lub dziesiątek tysięcy) traktujemy 
# jak powtórzony rząd jedności (lub dziesiątek), z dodanym słowem "tysiąc" w odpowiedniej odmianie gramatycznej.
# Liczbę zapisaną słownie budujemy za pomocą 3 funkcji bazowych, pobrana liczba jest sprawdzana
# i w zależności od jej długości wywołujemy odpowiednie kolejności 3 funkcji bazowych.
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
# PRZYKŁADOWY PRZEBIEG programu dla liczby 345111.20:
# 1. Pobranie liczby
# 2. Formatowanie liczby
# 3. Sprawdzenie poprawności liczby
# 4. Rozdzielenie liczby na zlotowki, grosze
# 5. Sprawdzenie długości liczby złotówek
# 6. Dla liczby 6 cyfrowej, 345111:
#     - dla 1. znaku odczytaj_setki('3')
#     - dla 2. i 3. znaku odczytaj_dziesiatki('45')
#         - wartość 45 czyli slownik_dziesiatki('4') + slownik_jednosci('5')
#     - dodaj slowo_tysiac()
#     - dla 4. znaku odczytaj_setki('1')
#     - dla 5. i 6. znaku odczytaj_dziesiatki('11')
#         - wartość 11 czyli slownik_kilkanascie('11')
#     - dodaj slowo_zlotych(zlotowki)
# 7. Sprawdzenie długości liczby groszy
# 8. Dla liczby 2 cyfrowej, 20:
#     - dla 1. i 2. znaku odczytaj_dziesiatki('20')
#         - wartość 20 czyli slownik_dziesiatki('20')
#     - dodaj slowo_groszy(grosze)

# #############################################################################
# Słowniki zawierają słowa kolejnych rzędów liczb
def slownik_jednosci(x: str):
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

def slownik_kilkanascie(x: str):
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

def slownik_dziesiatek(x: str):
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

def slownik_setek(x: str):
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

# #############################################################################
def slowo_zlotych(x: str):
    """
    Funkcja dbająca o poprawną końcówkę słowa "złote".
    """
    if int(x) < 10:
        zlotych = {'0': 'złotych',
                '1': 'złoty',
                '2': 'złote',
                '3': 'złote',
                '4': 'złote',
                '5': 'złotych',
                '6': 'złotych',
                '7': 'złotych',
                '8': 'złotych',
                '9': 'złotych'}
        return zlotych[x[-1]]
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

def slowo_groszy(x: str):
    """
    Funkcja dbająca o poprawną końcówkę słowa "groszy".
    """
    if int(x) < 10:
        groszy = {'0': 'groszy',
                '1': 'grosz',
                '2': 'grosze',
                '3': 'grosze',
                '4': 'grosze',
                '5': 'groszy',
                '6': 'groszy',
                '7': 'groszy',
                '8': 'groszy',
                '9': 'groszy'}
        return groszy[x[-1]]
    elif 10 <= int(x) < 20:
        return 'groszy'
    elif int(x)>= 20:
        groszy = {'0': 'groszy',
                '1': 'groszy',
                '2': 'grosze',
                '3': 'grosze',
                '4': 'grosze',
                '5': 'groszy',
                '6': 'groszy',
                '7': 'groszy',
                '8': 'groszy',
                '9': 'groszy'}
        return groszy[x[-1]]

def slowo_tysiecy(x: str):
    """
    Funkcja dbająca o poprawną końcówkę słowa "tysiąc".
    """
    if int(x) < 10:
        tysiecy = {'0': 'tysięcy ',
                '1': 'tysiąc ',
                '2': 'tysiące ',
                '3': 'tysiące ',
                '4': 'tysiące ',
                '5': 'tysięcy ',
                '6': 'tysięcy ',
                '7': 'tysięcy ',
                '8': 'tysięcy ',
                '9': 'tysięcy '}
        return tysiecy[x[-1]]
    elif 10 <= int(x) < 20:
        return 'tysięcy '
    elif int(x) >= 20:
        tysiecy = {'0': 'tysięcy',
                '1': 'tysięcy',
                '2': 'tysiące ',
                '3': 'tysiące ',
                '4': 'tysiące ',
                '5': 'tysięcy ',
                '6': 'tysięcy ',
                '7': 'tysięcy ',
                '8': 'tysięcy ',
                '9': 'tysięcy '}
        return tysiecy[x[-1]]

def slowo_milionow(x: str):
    """
    Funkcja dbająca o poprawną końcówkę słowa "milion".
    """
    if int(x) < 10:
        milionow = {'0': 'milionów ',
                '1': 'milion ',
                '2': 'miliony ',
                '3': 'miliony ',
                '4': 'miliony ',
                '5': 'milionów ',
                '6': 'milionów ',
                '7': 'milionów ',
                '8': 'milionów ',
                '9': 'milionów '}
        return milionow[x[-1]]
    elif 10 <= int(x) < 20:
        return 'milionów '
    elif int(x) >= 20:
        milionow = {'0': 'milionów ',
                '1': 'milionów ',
                '2': 'miliony ',
                '3': 'miliony ',
                '4': 'miliony ',
                '5': 'milionów ',
                '6': 'milionów ',
                '7': 'milionów ',
                '8': 'milionów ',
                '9': 'milionów '}
        return milionow[x[-1]]

# #############################################################################
# Funcje bazowe
def odczytaj_jednosci(x: str):
    """
    Powinna otrzymać tylko 1 cyfrę odpowiadającą pozycji jedności,
    przesyła ją do słownika i zwraca odpowiednie slowo.
    """
    return slownik_jednosci(x)

def odczytaj_dziesiatki(x: str):
    """
    Powinna otrzymać 2 znaki odpowiadające pozycji dziesiątek i jedności,
    przesyła znaki do odpowiedniego słownika i zwraca odpowiednie slowo.
    """
    if int(x) == 0:                     # 0
        slowo = ''
    elif int(x) < 10:                   # 1,2,3,4,5,6,7,8,9
        slowo=slownik_jednosci(x[1])
    elif int(x) > 10 and int(x) < 20:   # 11,12,13,14,15,16,17,18,19
        slowo=slownik_kilkanascie(x)
    elif int(x) % 10 == 0:              # 10,20,30,40,50,60,70,80,90
        slowo=slownik_dziesiatek(x[0])
    else:                               # 21+
        slowo=slownik_dziesiatek(x[0])
        slowo+=slownik_jednosci(x[1])
    return slowo

def odczytaj_setki(x: str):
    """
    Powinna otrzymać tylko 1 znak odpowiadający pozycji setek,
    przesyła go do słownika i zwraca odpowiednie slowo.
    """
    slowo=slownik_setek(x)
    return slowo

# #############################################################################
def przywitaj():
    """
    Funkcja witająca użytkownika.
    """
    wiadomosc = """Program zamieniający kwotę liczbową na słowną. Pełne nazewnictwo złotych i groszy.

Można wpisywać:
 1234        1234
1 234       1 234
1 234.0     1 234,0
1 234.7     1 234,7
1 234.70    1 234,70
1 234.706   1 234,706

Zakres 0 - 999 999 999
    """
    print(wiadomosc)

def pobierz_liczbe() -> str:
    """
    Pobiera liczbę od użytkownika.
    """
    liczba=''
    while not liczba:
        liczba = input('Podaj liczbę: ')
    return liczba

def formatuj_liczbe(liczba: str) -> str:
    """
    Pozbywa się białych znaków z podanego przez użytkownika łańcucha znaków. Zamienia ',' na '.'
    Przykład '1 234,56' -> '1234.56'
    """
    liczba = liczba.strip()
    while ' ' in liczba:
        liczba = liczba.replace(' ', '')
    if ',' in liczba:
        liczba = liczba.replace(',', '.')
    return liczba

def sprawdz_liczbe(liczba: str) -> bool:
    """
    Sprawdza czy liczba podana przez użytkownika jest rzeczywiście liczbą, np. czy nie zawiera liter.
    Przykład '1234.56' -> True
    Przykład '12$34a.56' -> False
    """
    try:
        float(liczba)
        if float(liczba) < 0 or float(liczba) > 999999999:
            raise ValueError
        else:
            return True
    except ValueError:
        print('liczba nieprawidłowa, konieczna liczba z zakresu 0 - 999 999 999', end = '')
        return False

def rozdziel_liczbe(liczba: str):
    """
    Rozdziela liczbę na część całkowitą (złotówki) i zmiennoprzecinkową (grosze).
    Przykład: liczba = '1234.56'-> zlotowki = '1234', grosze = '56'
    """
    liczba = float(liczba)
    zlotowki = str(int(liczba)) # pozostawienie części całkowitej i konwersja na str -> '1234'
    grosze = liczba % 1         # część zmiennoprzecinkowa, np 0.5599999999999454
    grosze = str(int(round(grosze, 2) * 100)) # po zaokrągleniu i konwersji '56'
    return zlotowki, grosze

# #############################################################################
# main
def main():

    przywitaj()

    while True:
        liczba = pobierz_liczbe()
        liczba = formatuj_liczbe(liczba)
        liczba_poprawna = sprawdz_liczbe(liczba)

        slowo=''

        if liczba_poprawna:
            zlotowki, grosze = rozdziel_liczbe(liczba)

            # tworzenie słownej kwoty złotych
            dlugosc = len(zlotowki)
            if dlugosc == 1:
                slowo += odczytaj_jednosci(zlotowki)
            elif dlugosc == 2:
                slowo += odczytaj_dziesiatki(zlotowki)
            elif dlugosc == 3:
                slowo += odczytaj_setki(zlotowki[0])
                slowo += odczytaj_dziesiatki(zlotowki[1:])
            elif dlugosc == 4:
                slowo += odczytaj_jednosci(zlotowki[0])
                slowo += slowo_tysiecy(zlotowki[0])
                slowo += odczytaj_setki(zlotowki[1])
                slowo += odczytaj_dziesiatki(zlotowki[2:])
            elif dlugosc == 5:
                slowo += odczytaj_dziesiatki(zlotowki[0:2])
                slowo += slowo_tysiecy(zlotowki[0:2])
                slowo += odczytaj_setki(zlotowki[2])
                slowo += odczytaj_dziesiatki(zlotowki[3:])
            elif dlugosc == 6:
                slowo += odczytaj_setki(zlotowki[0])
                slowo += odczytaj_dziesiatki(zlotowki[1:3])
                slowo += slowo_tysiecy(zlotowki[0:3])
                slowo += odczytaj_setki(zlotowki[3])
                slowo += odczytaj_dziesiatki(zlotowki[4:])
            elif dlugosc == 7:
                slowo += odczytaj_jednosci(zlotowki[0])
                slowo += slowo_milionow(zlotowki[0])
                slowo += odczytaj_setki(zlotowki[1])
                slowo += odczytaj_dziesiatki(zlotowki[2:4])
                slowo += slowo_tysiecy(zlotowki[1:4])
                slowo += odczytaj_setki(zlotowki[4])
                slowo += odczytaj_dziesiatki(zlotowki[5:])
            elif dlugosc == 8:
                slowo += odczytaj_dziesiatki(zlotowki[0:2])
                slowo += slowo_milionow(zlotowki[0:2])
                slowo += odczytaj_setki(zlotowki[2])
                slowo += odczytaj_dziesiatki(zlotowki[3:5])
                slowo += slowo_tysiecy(zlotowki[2:5])
                slowo += odczytaj_setki(zlotowki[5])
                slowo += odczytaj_dziesiatki(zlotowki[6:])
            elif dlugosc == 9:
                slowo += odczytaj_setki(zlotowki[0])
                slowo += odczytaj_dziesiatki(zlotowki[1:3])
                slowo += slowo_milionow(zlotowki[0:3])
                slowo += odczytaj_setki(zlotowki[3])
                slowo += odczytaj_dziesiatki(zlotowki[4:6])
                slowo += slowo_tysiecy(zlotowki[3:6])
                slowo += odczytaj_setki(zlotowki[6])
                slowo += odczytaj_dziesiatki(zlotowki[7:])

            # dodaj końcówkę 'złotych' w odpowiedniej formie
            slowo += slowo_zlotych(zlotowki)

            # tworzenie słownej kwoty groszy
            slowo += ' '
            dlugosc = len(grosze)
            if dlugosc == 1:
                slowo += odczytaj_jednosci(grosze)
            elif dlugosc == 2:
                slowo += odczytaj_dziesiatki(grosze)

            # dodaj końcówkę 'groszy' w odpowiedniej formie
            slowo += slowo_groszy(grosze)

        print(slowo)

if __name__ == "__main__":
    main()
