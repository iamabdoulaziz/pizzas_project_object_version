class EtreVivant:
    def print_infos(self):
        print("Je suis un être vivant;")

class Predator:
    def chasser_et_manger_proie(self):
        print("miam miam")

class Lion(EtreVivant, Predator):
    def print_infos(self):
        print("Je suis un lion.")

class Person(EtreVivant):
    def print_infos(self):
        print("je suis une personne")


lion = Lion()
lion.print_infos()
lion.chasser_et_manger_proie()