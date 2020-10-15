__all__ = ['order', 'shipper', 'shipping_cost']
from strategy.order import Order
from strategy.shipping_cost import ShippingCost
from strategy.fedex_strategy import FedexStrategy
from strategy.ups_strategy import UPSStrategy
from strategy.postal_strategy import PostalStrategy