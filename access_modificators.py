# Public, private, protected
# Public : Accès de l'interieur et l'exterieur de la classe
# Private : Accès de l(intérieur de la classe uniquement on met (__) devant la variable pour la rendre privé
# Protected : Accès depuis l'interieur de la classes et des dérivées
# Pour rendre protected ( _a )


class Person:
    def __init__(self, name):
        # Par defaut la variable est publique mais on peut la rendre privé c'est à dire l'utilisé que dans la classe

        # self.name = name
        self._name = name # Je le rends protected (_name)

    def print_infos(self):
        print(f"Je m'appelle {self._name}.")

class Etudiant(Person):
    def print_infos(self):
        print(f"Je suis un étudiant, je m'appelle {self._name}")


person1 = Etudiant('Cute boy ')

person = Person("Star")
person.name = "Abdoul"
person.print_infos()
