"""
Objects - instance of a class. Any entity that has a state and behavior
class - collection of objects
Inheritance - acquires all the properties and behaviours of a parent object
Polymorphism - one task is performed in different ways. Overloading and overriding is used
Abstraction - hiding internal details and showing functionality
Encapsulation - Binding code and data together into a single unit 
"""

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self) -> str:
        return f"{self.name} will {self.speed}/hr"
    
    def travel(self, speed):
        return f"{self.name} will travel {self.speed}km/hr"
    
class Bmw(Car):
    def travel(self, speed=224):
        #return f"{self.name} go {speed}"
        return super().travel(speed)
    

bmw = Bmw("Class A", 124)
print(bmw.travel(300)) # returns the speed as 300
