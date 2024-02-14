class Fruits:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def onyesha(self):
        print(f"My favorite fruits are {self.name} which is of price KSH {self.price} ")

myobject = Fruits( "Apples", 200)
myobject.onyesha()
myobject = Fruits( "Mangoes", 80)
myobject.onyesha()
myobject = Fruits( "Bananas", 50)
myobject.onyesha()
myobject = Fruits( "Grapes", 600)
myobject.onyesha()
myobject = Fruits( "Oranges", 240)
myobject.onyesha()



