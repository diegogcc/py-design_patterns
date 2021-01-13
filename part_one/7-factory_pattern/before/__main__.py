from chevy_volt import ChevyVolt
from ford_focus import FordFocus
from jeep_sahara import JeepSahara
from nullcar import NullCar

def get_car(carname):
    if carname == 'Chevy':
        return ChevyVolt()
    elif carname == 'Ford':
        return FordFocus()
    elif carname == 'Jeep':
        return JeepSahara()
    else:
        return NullCar(carname)

for carname in 'Chevy', 'Ford', 'Jeep', 'Tesla':
    car = get_car(carname)
    car.start()
    car.stop()

    # Chevrolet Volt  runing with shocking power!
    # Chevrolet Volt shutting down
    # Cool Ford Focus running smoothly
    # Ford Focus shutting down.
    # Jeep Sahara running ruggedly
    # Jeep Sahara shutting down
    # Unknown car "Tesla".