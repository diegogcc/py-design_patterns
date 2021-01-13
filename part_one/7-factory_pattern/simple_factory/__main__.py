from auto_factory import AutoFactory

factory = AutoFactory()

for carname in 'ChevyVolt', 'FordFocus', 'JeepSahara', 'Tesla':

    car = factory.create_instance(carname)
    car.start()
    car.stop()

    # Chevrolet Volt  runing with shocking power!
    # Chevrolet Volt shutting down
    # Cool Ford Focus running smoothly
    # Ford Focus shutting down.
    # Jeep Sahara running ruggedly
    # Jeep Sahara shutting down
    # Unknown car "Tesla".