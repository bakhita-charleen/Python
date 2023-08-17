#
#Objects are instances for class
class Students:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def sayhello(self):
        print("My name is ", self.name,"I'm ", self.age, "years ","and I'm a ", self.gender)
myobje = Students("Charleen", "Female", 4)

myobje.sayhello()
