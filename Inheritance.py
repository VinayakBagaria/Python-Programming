class Parent:
    counter=10
    def __init__(self):
        print('Class Initialised')
    def parentFunc(self):
        print('Parent Func being called')
    def setCounter(self,num):
        Parent.counter=num
    def showCounter(self):
        print(Parent.counter)

class Child(Parent):
    def __init__(self):
        print("Child class initialised")
    def childMethod(self):
        print("Child func called")

c=Child()
c.childMethod()
c.parentFunc()
c.setCounter(20)
c.showCounter()