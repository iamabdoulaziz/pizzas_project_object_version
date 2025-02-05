# Let's start the project


class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def print(self):
        print(f"PIZZA {self.name} : {self.price}")


pizza = Pizza("4 fromages", 8.5)
pizza.print()
