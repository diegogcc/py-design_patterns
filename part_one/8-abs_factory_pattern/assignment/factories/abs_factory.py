from abc import ABCMeta, abstractmethod

class AbsFactory(metaclass=ABCMeta):

    @abstractmethod
    def create_commercial(self):
        pass

    @abstractmethod
    def create_government(self):
        pass

    @abstractmethod
    def create_retail(self):
        pass