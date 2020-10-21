from abs_builder import AbsBuilder

class MyPizza(AbsBuilder):

    def make_crust(self):
        self._pizza.crust = 'Whole Wheat'

    def add_sauce(self):
        self._pizza.sauce = 'Tomato'

    def add_meat(self):
        self._pizza.meat = 'Pepperoni'

    def add_veggies(self):
        self._pizza.veggies = 'Tomatoes'

    def add_cheese(self):
        self._pizza.cheese = 'Mozzarela'