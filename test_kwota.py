import unittest
import kwota

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'kwota.py'."""

    def test_slowo_zlotych01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_zlotych('1'), 'złoty')

    def test_slowo_zlotych02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_zlotych('10'), 'złotych')

    def test_slowo_zlotych03(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_zlotych('22'), 'złote')

    def test_slowo_groszy01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_groszy('1'), 'grosz')

    def test_slowo_groszy02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_groszy('11'), 'groszy')

    def test_slowo_groszy03(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_groszy('73'), 'grosze')

    def test_slowo_tysiecy01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_tysiecy('2'), 'tysiące ')

    def test_slowo_tysiecy02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_tysiecy('20'), 'tysięcy ')

    def test_slowo_tysiecy03(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_tysiecy('24'), 'tysiące ')

    def test_slowo_milionow01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_milionow('1'), 'milion ')

    def test_slowo_milionow02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_milionow('15'), 'milionów ')

    def test_slowo_milionow03(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.slowo_milionow('47'), 'milionów ')

    def test_odczytaj_jednosci01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_jednosci('0'), 'zero ')

    def test_odczytaj_jednosci02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_jednosci('3'), 'trzy ')

    def test_odczytaj_dziesiatki01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_dziesiatki('0'), '')

    def test_odczytaj_dziesiatki02(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_dziesiatki('06'), 'sześć ')

    def test_odczytaj_dziesiatki03(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_dziesiatki('12'), 'dwanaście ')

    def test_odczytaj_dziesiatki04(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_dziesiatki('20'), 'dwadzieścia ')

    def test_odczytaj_dziesiatki05(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_dziesiatki('35'), 'trzydzieści pięć ')

    def test_odczytaj_setki01(self):
        """Czy funkcja zwraca odpowiednią wartość?"""
        self.assertEqual(kwota.odczytaj_setki('3'), 'trzysta ')

    def test_formatuj_liczbe01(self):
        """Czy dane w postaci '1 234 567,89' są prawidłowo obsługiwane?"""
        sformatowana_liczba = kwota.formatuj_liczbe('1 234 567,89')
        self.assertEqual(sformatowana_liczba, '1234567.89')

    def test_sprawdz_liczbe_01(self):
        """Czy dane w postaci '0' są uznane za poprawną liczbę?"""
        self.assertTrue(kwota.sprawdz_liczbe('0'))

    def test_sprawdz_liczbe_02(self):
        """Czy dane w postaci '.5' są uznane za poprawną liczbę?"""
        self.assertTrue(kwota.sprawdz_liczbe('.5'))

    def test_sprawdz_liczbe_03(self):
        """Czy dane w postaci '1234.56' są uznane za poprawną liczbę?"""
        self.assertTrue(kwota.sprawdz_liczbe('1234.56'))

    def test_sprawdz_liczbe_04(self):
        """Czy dane w postaci '1aa' są uznane za niepoprawną liczbę?"""
        self.assertFalse(kwota.sprawdz_liczbe('1aa'))

    def test_sprawdz_liczbe_05(self):
        """Czy dane w postaci '-1' są uznane za niepoprawną liczbę?"""
        self.assertFalse(kwota.sprawdz_liczbe('-1'))

    def test_sprawdz_liczbe_06(self):
        """Czy dane w postaci '1000222333' są uznane za niepoprawną liczbę?"""
        self.assertFalse(kwota.sprawdz_liczbe('1000222333'))

    def test_rozdziel_liczbe01(self):
        """Czy liczba w postaci '1234' jest prawidłowo rozdzielana?"""
        self.assertEqual(kwota.rozdziel_liczbe('1234'), ('1234', '0'))

    def test_rozdziel_liczbe02(self):
        """Czy liczba w postaci '1234.' jest prawidłowo rozdzielana?"""
        self.assertEqual(kwota.rozdziel_liczbe('1234.'), ('1234', '0'))

    def test_rozdziel_liczbe03(self):
        """Czy liczba w postaci '1234.5' jest prawidłowo rozdzielana?"""
        self.assertEqual(kwota.rozdziel_liczbe('1234.5'), ('1234', '50'))

    def test_rozdziel_liczbe04(self):
        """Czy liczba w postaci '1234.56' jest prawidłowo rozdzielana?"""
        self.assertEqual(kwota.rozdziel_liczbe('1234.56'), ('1234', '56'))

    def test_rozdziel_liczbe05(self):
        """Czy liczba w postaci '1234.567' jest prawidłowo rozdzielana?"""
        self.assertEqual(kwota.rozdziel_liczbe('1234.567'), ('1234', '57'))

    def test_slownie_zlotych01(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('0'),
            'zero złotych')

    def test_slownie_zlotych02(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('1'),
            'jeden złoty')

    def test_slownie_zlotych03(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('10'),
            'dziesięć złotych')

    def test_slownie_zlotych04(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('11'),
            'jedenaście złotych')

    def test_slownie_zlotych05(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('20'),
            'dwadzieścia złotych')

    def test_slownie_zlotych06(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('44'),
            'czterdzieści cztery złote')

    def test_slownie_zlotych07(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('100'),
            'sto złotych')

    def test_slownie_zlotych08(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('505'),
            'pięćset pięć złotych')

    def test_slownie_zlotych09(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('719'),
            'siedemset dziewiętnaście złotych')

    def test_slownie_zlotych10(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('667'),
            'sześćset sześćdziesiąt siedem złotych')

    def test_slownie_zlotych11(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('1000'),
            'jeden tysiąc złotych')

    def test_slownie_zlotych12(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('2500'),
            'dwa tysiące pięćset złotych')

    def test_slownie_zlotych13(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('9017'),
            'dziewięć tysięcy siedemnaście złotych')

    def test_slownie_zlotych14(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('11000'),
            'jedenaście tysięcy złotych')

    def test_slownie_zlotych15(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('98764'),
            'dziewięćdziesiąt osiem tysięcy siedemset sześćdziesiąt cztery złote')

    def test_slownie_zlotych16(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('200000'),
            'dwieście tysięcy złotych')

    def test_slownie_zlotych17(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('440502'),
            'czterysta czterdzieści tysięcy pięćset dwa złote')

    def test_slownie_zlotych18(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('1000000'),
            'jeden milion złotych')

    def test_slownie_zlotych19(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('5000105'),
            'pięć milionów sto pięć złotych')

    def test_slownie_zlotych20(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('1002000'),
            'jeden milion dwa tysiące złotych')

    def test_slownie_zlotych21(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('25000100'),
            'dwadzieścia pięć milionów sto złotych')

    def test_slownie_zlotych22(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('810015015'),
            'osiemset dziesięć milionów piętnaście tysięcy piętnaście złotych')

    def test_slownie_zlotych23(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('123456789'),
            'sto dwadzieścia trzy miliony czterysta pięćdziesiąt sześć tysięcy'
            + ' siedemset osiemdziesiąt dziewięć złotych')

    def test_slownie_zlotych24(self):
        """Czy liczba jest prawidłowo zamieniana na postać słowną?"""
        self.assertEqual(kwota.slownie_zlotych('999999999'),
            'dziewięćset dziewięćdziesiąt dziewięć milionów dziewięćset dziewięćdziesiąt' 
            + ' dziewięć tysięcy dziewięćset dziewięćdziesiąt dziewięć złotych')

    def test_slownie_groszy01(self):
        """Czy liczba '0' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('0'), 'zero groszy')

    def test_slownie_groszy02(self):
        """Czy liczba '1' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('1'), 'jeden grosz')

    def test_slownie_groszy03(self):
        """Czy liczba '2' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('2'), 'dwa grosze')

    def test_slownie_groszy04(self):
        """Czy liczba '5' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('5'), 'pięć groszy')

    def test_slownie_groszy05(self):
        """Czy liczba '10' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('10'), 'dziesięć groszy')

    def test_slownie_groszy06(self):
        """Czy liczba '19' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('19'), 'dziewiętnaście groszy')

    def test_slownie_groszy07(self):
        """Czy liczba '62' jest prawidłowo zamieniana?"""
        self.assertEqual(kwota.slownie_groszy('62'), 'sześćdziesiąt dwa grosze')

unittest.main()
