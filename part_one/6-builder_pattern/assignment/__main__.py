from pizza_maker import PizzaMaker
from my_pizza import MyPizza

pizza_maker = PizzaMaker(MyPizza())
pizza_maker.make_pizza()
pizza = pizza_maker.get_pizza()
pizza.display()

# Custom Pizza:
#              Crust: Whole Wheat
#               Base: Tomato
#         Meat Toppings: Pepperoni
#         Vegetable Toppings: Tomatoes
#         Cheese Toppings: Mozzarela