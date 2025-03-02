
class Person:
    TYPE = "Humain"
    def __init__(self, name):
        self.name = name

    #Methode d'instance car cette methode utilise le self et lui permet d'acceder aux données de l'objet
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.name)} - {self.TYPE}")
    #Premier charactère en majuscule
    # Ceci est une methode statique car elle ne depend de rien, pas de self
    @staticmethod
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    # Ceci est une methode de classe
    @classmethod
    def methode_classe(cls):
        print("Methode de classe :" + cls.TYPE)

person1 = Person("abdoul Aziz")
person1.se_presenter()

print(person1.formater_chaine("toTO"))

Person.methode_classe()
