class Fruit:
    def __init__(self, name, price):
        self.name=name
        self.price=price
    def display(self):
        print(f"My favorite fruit is {self.name} and it costs {self.price}")
c1=Fruit("pineapple","50ksh")
c1.display()
c2=Fruit("apple","30ksh")
c2.display()
c3=Fruit("mango","40ksh")
c3.display()
c4=Fruit("orange","20ksh")
c4.display()
c5=Fruit("grapes","50ksh")
c5.display()