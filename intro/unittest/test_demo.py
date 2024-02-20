import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Se ruleaza metoda setUp()")

    def tearDown(self):
        print("Se ruleaza metoda tearDown()")

    def test_1(self):
        print("Pas 1")
        print("Pas 2")
        print("Pas 3")
        # assert 1 + 1 == 3, "Conditia ca testul sa treaca nu a fost indeplinita"
        self.assertTrue(1 + 1 == 2, "Conditia ca testul sa treaca nu a fost indeplinita")

    def test_2(self):
        print("Se ruleaza test 2")
        self.metoda_auxiliara()

        lista_expectata = [0, 1, 2, 3]
        lista_actuala = [0, 1, 2, 3]
        # assert lista_expectata == lista_actuala, "Mesaj de eroare"
        self.assertEqual(lista_expectata, lista_actuala, "Mesaj de eroare")


    def test_3(self):
        print("Se ruleaza test 3")
        lista_actuala = [0, 1, 3, 2]
        a = 1
        # assert a in lista_actuala
        self.assertIn(a, lista_actuala, "Mesaj de eroare")


    def metoda_auxiliara(self):
        print("Se ruleaza metoda auxiliara")