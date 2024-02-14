class Car:

    def __init__(self, make, model, year , color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def onyesha(self):
        print(f"My dream car is a {self.make} model {self.model} manufactured in {self.year} and its color is {self.color}")

myobject = Car("porsche", "GT-3", 2024 , "blue")
myobject.onyesha()

