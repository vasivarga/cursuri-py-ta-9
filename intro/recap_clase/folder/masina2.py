class MasinaPlus:
    viteza_maxima = 250
    viteza_curenta = 0
    este_pornita = False

    def __init__(self, model, marca, an_fabricatie):
        self.model = model
        self.marca = marca
        self.an_fabricatie = an_fabricatie


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