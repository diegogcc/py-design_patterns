from factories.ford_factory import FordFactory
from factories.gm_factory import GMFactory

for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()
    car = factory.create_sport()
    car.start()
    car.stop()
    car = factory.create_luxury()
    car.start()
    car.stop()


# Ford Fiesta running cheaply
# Ford Fiesta shutting down
# Ford Mustang ready to go
# Ford Mustang shutting down
# Lincoln MKS running smoothly
# Lincoln MKS shutting down
# Chevy Spark running efficiently.
# Chevy Spark shutting down
# Chevy Camaro sounding awesome
# Chevy Camaro shutting down
# Cadillac CTS purring
# Cadillac CTS shutting down