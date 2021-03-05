from abc import ABCMeta, abstractmethod

class AbsFacade(metaclass=ABCMeta):

    @abstractmethod
    def get_employees(self):
        pass