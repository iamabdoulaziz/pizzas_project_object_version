class EtreVivant:
    def print_infos(self):
        print("Je suis un être vivant;")

class Chat(EtreVivant):
    def print_infos(self):
        print("Je suis un chat.")

class Person(EtreVivant):
    def print_infos(self):
        print("je suis une personne")

l = [EtreVivant(), Chat(), Person()]

for e in l:
    e.print_infos()

def additionner(a, b):
    somme = 0
    if isinstance(a, int):
        somme += a
    if isinstance(a, str):
        somme += len(a)
    if isinstance(b, int):
        somme += b
    if isinstance(b, str):
        somme += len(b)
    return  somme

print (additionner(5, "aaaa"))