from factories import loader

for factory_name in 'chevy_factory', 'ford_factory', 'jeep_factory', 'tesla_factory':

    factory = loader.load_factory(factory_name)
    car = factory.create_auto()

    car.start()
    car.stop()


# Chevy Volt running with shocking power!
# Chevy Volt shutting down
# Ford Focus running cooly
# Ford Focus stopping
# Jeep Sahara running ruggedly
# Jeep Sahara shutting down
# Unknown car "Unknown"