class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        if not isinstance(age, int):
            print("l'age doit être de type int ")
            self.age = 0


    def print_infos(self):
        print(f" Je m'appelle {self.name}.")
        if self.age > 0:
            print(f"L'an prochain j'aurai {self.age + 1} ans.")


person = Person("Cute boy", 22)
person.print_infos()
