# I add new parameters like ingredients, vegetarien, and modified the print method
# On comments it is my own code before checking the solution


class Pizza:
    def __init__(self, name, price, ingredients, vegetarian = False): # vegetarian = ""
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarien = vegetarian



    def print(self):
        veg_str = ""
        if self.vegetarien:
            veg_str = "- VEGETARIAN"
            #print(f"PIZZA {self.name} : {self.price} euros - VEGETARIAN")
        # else:
        #     print(f"PIZZA {self.name} : {self.price} euros")
        print(f"PIZZA {self.name} : {self.price} euros {veg_str}")
        print(", ".join(self.ingredients))
        print()


# Pizza("4 fromages", 8.5, ("bris", "emmental", "compté", "parnesan"))
# pizza.print()

pizzas = (
    Pizza("4 fromages", 8.5, ("bris", "emmental", "compté", "parnesan"), True),
    Pizza("Cutence Pizza", 10.5, ("farine", "fromage", "poulet", "tomates")),
    Pizza("Cute_girl P", 12.5, ("Cho", "banane plantin", "poulet", "huile d'olive")),
    Pizza("Végétarienne", 7.8, ("Champignons", "tomate", "oignons", "poivrons"), True),

)

for pizz in pizzas:
    pizz.print()

