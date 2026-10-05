from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self = ""):
        pass
class HomoSapien(Animal):
    def move(self = ""):
        print("High IQ")

class Froglet(Animal):
    def move(self = ""):
        print("Has legs that leap.")

class Duck(Animal):
    def move(self = ""):
        print("Quacks a lot.")

class Cheetah(Animal):
    def move(self=""):
        print("Runs so fast he'll eat you within the blink of an eye!")

for obj in HomoSapien, Froglet, Duck, Cheetah:
    obj1 = obj()
    obj1.move()
