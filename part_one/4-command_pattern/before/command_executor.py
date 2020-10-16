class CommandExecutor:

    def execute_command(self, args):
        if args[0] == 'CreateOrder':
            self.create_order()
        elif args[0] == 'UpdateQuantity':
            self.update_quantity(args[1])
        elif args[0] == 'ShipOrder':
            self.ship_order()
        else:
            print('Unrecognized command: {}'.format(args[0]))

    def create_order(self):
        pass

    def update_quantity(self, value):
        print(value)
        old_val = 5
        print('Database updated')
        print('Logging update quantity from %s to %s' % (old_val, value))

    def ship_order(self):
        pass