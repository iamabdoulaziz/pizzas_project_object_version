


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_infos(self):
        print(f"Je m'appelle {self.name}, j'ai {self.age} ans.")

    # def __str__(self):
    #     return "STR" #str(self.__dict__)

    # def __repr__(self):
    #     return "REPR"

    def __repr__(self):
        return __class__.__name__ + "" + str(self.__dict__)

person1 = Person("Cute boy", 22)
person1.print_infos()

print(person1)
