from abc import ABCMeta, abstractmethod
from pizza import Pizza

class AbsBuilder(metaclass=ABCMeta):

    def get_pizza(self):
        return self._pizza

    def new_pizza(self):
        self._pizza = Pizza()

    @abstractmethod
    def make_crust(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_meat(self):
        pass

    @abstractmethod
    def add_veggies(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass