from order import Order
from shipping_cost import ShippingCost
from fedex_strategy import FedExStrategy
from usps_strategy import USPSStrategy
from ups_strategy import UPSStrategy

# Test Fedex
order = Order("FEDEX")
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test USPS
order = Order("USPS")
strategy = USPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

# Test UPS
order = Order("UPS")
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

print("Tests passed")
