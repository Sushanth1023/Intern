from abc import ABC, abstractmethod

class AbstractTrial(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def sleep(self):
        print("Sleeping")
class Dog(AbstractTrial):
    def __init__(self):
        print("Bow Bow")

class Cat(AbstractTrial):
    def __init__(self):
        print("Meow Meow")    

dog=Dog()
dog.sleep()
cat=Cat()
cat.sleep()

