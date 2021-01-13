from abc import ABCMeta, abstractmethod

class AbsCust(metaclass=ABCMeta):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abstractmethod
    def send_invoice(self):
        pass