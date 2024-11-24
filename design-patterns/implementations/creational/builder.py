from enum import Enum


class BaseType(Enum):
    REGULAR = "Regular"
    PAN_TOSSED = "Pan Tossed"
    THIN_CRUST = "Thin Crust"
    CHEESE_BURST = "Cheese Burst"


class Pizza:
    def __init__(self):
        self.base: BaseType = BaseType.REGULAR
        self.extra_cheese = False
        self.corn = True
        self.pepperoni = False
        self.chicken = False
        self.veggies = False

    def __str__(self):
        return (
            f"Base: {self.base.name}, "  
            f"Extra Cheese: {'Yes' if self.extra_cheese else 'No'}, "  
            f"Corn: {'Yes' if self.corn else 'No'}, "  
            f"Pepperoni: {'Yes' if self.pepperoni else 'No'}, "  
            f"Chicken: {'Yes' if self.chicken else 'No'}, "  
            f"Veggies: {'Yes' if self.veggies else 'No'}"
        )


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def change_base(self, base_type: BaseType):
        self.pizza.base = base_type
        return self

    def add_cheese(self):
        self.pizza.extra_cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_chicken(self):
        self.pizza.chicken = True
        return self

    def add_veggies(self):
        self.pizza.veggies = True
        return self

    def get(self):
        return self.pizza


if __name__ == '__main__':
    basic_pizza = PizzaBuilder().get()
    print(basic_pizza)

    pepperoni_pizza = PizzaBuilder().change_base(BaseType.THIN_CRUST).add_pepperoni().add_cheese().get()
    print(pepperoni_pizza)

    veggie_delight = PizzaBuilder().change_base(BaseType.CHEESE_BURST).add_veggies().get()
    print(veggie_delight)
