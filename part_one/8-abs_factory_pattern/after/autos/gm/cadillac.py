from autos.abs_auto import AbsAuto

class CadillacCTS(AbsAuto):

    def start(self):
        print('Cadillac CTS purring')

    def stop(self):
        print('Cadillac CTS shutting down')