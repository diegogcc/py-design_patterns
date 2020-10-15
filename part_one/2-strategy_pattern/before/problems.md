# PROBLEMS DISCOVERED

## Violation of the SRP

The class *Order* should not considered how it will be shipped.

## Violation of the OCP

We would need to modify the *ShippingCost* class in order to add a new shipping methods or shippers.

## Violation of the DIP

Since we are programming to a concrete class and method (the *ShippingCost* class and its *shipping_cost()* method)

## Long list of if/elif clauses 

Inside the *shipping_cost()* method