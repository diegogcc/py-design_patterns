class Pizza:

    def display(self):
        print('Custom Pizza:')
        print('\t{:>10}: {}'.format('Crust', self.crust))
        print('\t{:>10}: {}'.format('Base', self.sauce))
        print('\t{:>10}: {}'.format('Meat Toppings', self.meat))
        print('\t{:>10}: {}'.format('Vegetable Toppings', self.veggies))
        print('\t{:>10}: {}'.format('Cheese Toppings', self.cheese))