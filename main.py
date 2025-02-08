# I add new parameters like ingredients, vegetarien, and modified the print method
# On comments it is my own code before checking the solution


class Pizza:
    def __init__(self, name, price, ingredients, vegetarian = False): # vegetarian = ""
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian



    def print(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = "- VEGETARIAN"
            #print(f"PIZZA {self.name} : {self.price} euros - VEGETARIAN")
        # else:
        #     print(f"PIZZA {self.name} : {self.price} euros")
        print(f"PIZZA {self.name} : {self.price} euros {veg_str}")
        print(", ".join(self.ingredients))
        print()


class PersonalizedPizza(Pizza):
    BASIC_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    LAST_NUMBER = 0
    def __init__(self):
        PersonalizedPizza.LAST_NUMBER += 1
        self.pizza_number = PersonalizedPizza.LAST_NUMBER
        super().__init__(f"Personnalisée {self.pizza_number}", 0, [])
        self.ask_ingredients_to_user()
        self.calculate_price()
        #self.price = self.calculate_price()

    def ask_ingredients_to_user(self):
        print("---")
        print(f"Ingredients pour la pizza personnalisée {self.pizza_number}")
        while True:
            ingredient = input("Ajoute un ingrédient (ou ENTER pour terminer) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Tu as ajouté {len(self.ingredients)} ingrédients.s : {",".join(self.ingredients)}")
            #self.calculate_price()
            print()

    def calculate_price(self):
        #print(f"Prix de base = {self.BASIC_PRICE} euros")
        self.price = self.BASIC_PRICE + (self.PRICE_PER_INGREDIENT * len(self.ingredients))
        #calcule = self.BASIC_PRICE + (self.PRICE_PER_INGREDIENT*len(self.ingredients))
        #print(f"Le prix après ajout des ingrdients : {calcule} euros")
        #return calcule
# Pizza("4 fromages", 8.5, ("bris", "emmental", "compté", "parnesan"))
# pizza.print()

pizzas = [
    Pizza("4 fromages", 8.5, ("bris", "emmental", "compté", "parnesan"), True),
    Pizza("Cutence Pizza", 10.5, ("farine", "fromage", "poulet", "tomates")),
    Pizza("Cute girl P", 12.5, ("Cho", "banane plantin", "poulet", "huile d'olive")),
    Pizza("Végétarienne", 7.8, ("Champignons", "tomate", "oignons", "poivrons"), True),
    PersonalizedPizza(),
    PersonalizedPizza()
]
# Now let's sort pizzas, there is a problem we can't sort a tupple, so I transformed it to list
def tri(e):
    return e.price

#pizzas.sort(key=tri, reverse=True)

for pizz in pizzas:
    pizz.print()