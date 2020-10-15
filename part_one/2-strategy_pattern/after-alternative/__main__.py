from strategy import Order, ShippingCost

def fedex_strategy(order):
    return 3.0

ups_strategy = lambda order: 4.0

order = Order()

# Test Fedex shipping 

strategy = fedex_strategy
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test UPS shipping 

cost_calculator = ShippingCost(ups_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test Postal shipping 

cost_calculator = ShippingCost(lambda order: 5.0)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('tests passed')
