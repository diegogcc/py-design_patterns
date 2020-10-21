class PizzaMaker:

    def __init__(self, builder):
        self._builder = builder

    def get_pizza(self):
        return self._builder.get_pizza()
        
    def make_pizza(self):
        self._builder.new_pizza()
        self._builder.make_crust()
        self._builder.add_sauce()
        self._builder.add_meat()
        self._builder.add_veggies()
        self._builder.add_cheese()