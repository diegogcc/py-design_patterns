from abc import ABCMeta, abstractmethod

class AbsCust(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def report_type(self):
        pass