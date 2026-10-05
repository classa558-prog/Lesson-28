from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def yuwie(self):
        print("Hi : 3e3")
    def display_argument(self, argument):
        print(argument)
class SubClass(BaseClass):
    def yuwie(self):
        print("Hello 2198js")
    
obj1 = SubClass()
obj1.yuwie()
obj1.display_argument("hello. 344de3")
