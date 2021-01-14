from abc import ABCMeta, abstractstaticmethod

class AbsFactory(metaclass=ABCMeta):

    @abstractstaticmethod
    def create_economy(self):
        pass

    @abstractstaticmethod
    def create_sport(self):
        pass

    @abstractstaticmethod
    def create_luxury(self):
        pass