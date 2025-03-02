


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_infos(self):
        print(f"Je m'appelle {self.name}, j'ai {self.age} ans.")

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        return False

person1 = Person("Cute boy", 22)
person1.print_infos()

person2 = Person("Cute girl", 18)
person2.print_infos()

person3 = person1

print(person1 == person2)
print()
print(person1 is person2)

print(person1.__dict__ == person2.__dict__)

print(person1.__dict__)
