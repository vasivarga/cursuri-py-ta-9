class Masina:
    marca = None
    model = None
    an_fabricatie = None
    viteza_maxima = 250
    viteza_curenta = 0
    este_pornita = False

    def porneste_masina(self):
        print("Am pornit masina")
        self.este_pornita = True

    def accelerare_masina(self, viteza):
        # self.viteza_curenta = self.viteza_curenta + viteza
        if self.viteza_curenta + viteza < self.viteza_maxima:
            self.viteza_curenta += viteza
            print(f"Am accelerat cu {viteza}. Viteza curenta: {self.viteza_curenta}")
        else:
            self.viteza_curenta = self.viteza_maxima
            print(f"Ati atins viteza maxima. Viteza curenta: {self.viteza_curenta}")

    def decelerare_masina(self, viteza):
        if self.viteza_curenta - viteza >= 0:
            self.viteza_curenta -= viteza
            print(f"Am decelerat {viteza}. Viteza curenta: {self.viteza_curenta}")
        else:
            self.viteza_curenta = 0
            print(f"Ati atins viteza minima. Viteza curenta: {self.viteza_curenta}")

    def descriere(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"An fabricatie: {self.an_fabricatie}")

    @staticmethod
    def claxoneaza():
        print("tiiit tiit")


if __name__ == "__main__":

    masina1 = Masina()

    print(masina1.este_pornita)
    masina1.porneste_masina()
    print(masina1.este_pornita)

    masina1.accelerare_masina(150)
    masina1.accelerare_masina(90)
    masina1.accelerare_masina(30)

    masina1.decelerare_masina(210)

    print(masina1.viteza_curenta)

    masina1.decelerare_masina(50)
    print(masina1.viteza_curenta)

    masina1.accelerare_masina(100)


    masina2 = Masina()

    masina1.marca = "Volkswagen"
    masina2.marca = "Mercedes"

    masina1.an_fabricatie = 2012
    masina2.an_fabricatie = 2018

    masina1.model = "Golf 4"
    masina2.model = "C class"

    print(Masina.model)
    print(masina1.model)
    print(masina2.model)

    # assert masina1 == masina2


    masina1.descriere()

    masina2.descriere()


print("Cod in afara if-ului")