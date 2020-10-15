from strategy import Order, ShippingCost
from strategy import FedexStrategy, UPSStrategy, PostalStrategy

# Test Fedex shipping

order = Order()
strategy = FedexStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test UPS shipping

order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Postal shipping

order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('tests passed')