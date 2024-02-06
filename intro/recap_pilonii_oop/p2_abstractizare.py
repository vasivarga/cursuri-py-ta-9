from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def scoate_sunet(self):
        pass

class Pisica(Animal):
    def scoate_sunet(self):
        print("Pisica face miau")


class Caine(Animal):
    def scoate_sunet(self):
        print("Ham ham")


pisic_1 = Pisica()
pisic_1.scoate_sunet()

catel_1 = Caine()
catel_1.scoate_sunet()