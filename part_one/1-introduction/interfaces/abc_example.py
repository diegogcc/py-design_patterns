import abc

class MyABC(metaclass=abc.ABCMeta):
    """Abstract Base Class Definition"""

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class MyClass(MyABC):
    """Implementation of MyABC"""

    def __init__(self, value=None):
        self._my_prop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._my_prop *= 2 + value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._my_prop

class MyClassNotImplentedInterface(MyABC):
    """A class that doesn't implement the abstract methods"""
    pass


a = MyClass(value=42)
print(a.some_property)
a.do_something(value=41)
print(a.some_property)

#! Instantiation error if we use MyClassNotImplentedInterface 
# b = MyClassNotImplentedInterface()
#* TypeError: Can't instantiate abstract class