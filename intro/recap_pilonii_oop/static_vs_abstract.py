from abc import ABC, abstractmethod

from recap_pilonii_oop.p3_polimorfism import sir_numere_pare


class Animal(ABC):
    @abstractmethod
    def scoate_sunet(self):
        pass

    @staticmethod
    def merge():
        print("Animalul merge")


class Pisica(Animal):
    def scoate_sunet(self):
        print("Pisica face miau")


pisica1 = Pisica()
pisica1.scoate_sunet()

Pisica.merge()
Pisica.scoate_sunet() # da eroare


