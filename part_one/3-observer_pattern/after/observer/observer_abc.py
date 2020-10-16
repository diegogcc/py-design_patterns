from abc import ABCMeta, abstractmethod

class ABCObserver(metaclass=ABCMeta):

    @abstractmethod
    def update(self, value):
        pass
