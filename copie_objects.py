import copy



class Person:
    def __init__(self, name, age, amis):
        self.name = name
        self.age = age
        self.amis = amis

    def print_infos(self):
        print(f"Je m'appelle {self.name}, j'ai {self.age} ans.")
        print(f"Amis : {self.amis}")


person1 = Person("Cute boy", 22, ["La brute", "Mimich", "Arthur"])
person1.print_infos()
print("/////////")
print()

#person2 = Person("Cute girl", 18)
#person2 = copy.copy(person1) this is a shallow copy
person2 = copy.deepcopy(person1) # this is a deep cppy
person1.amis[0] = "Cute girl"
person2.print_infos()
print("/////////")
print()


person1.name = "Abdoul"
person1.print_infos()
print("/////////")

print()


person2.print_infos()
