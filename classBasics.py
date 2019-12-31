# __author__ = "Akash Maniar"
#
# import sys
# from mypackage.Car import *
# from mypackage.Person import Person
#
# person = Person()
# person.name = "Akash"
# person.sayhello()
# myCar = Car()
# truck = Truk()
# myCar.setSpeed(100)
# truck.setSpeed(60)
#
# print(sys.version)
# x = "My name is Ståle"
# print(bin(3))


class SomeClass:
    def __init__(self):
        self.arr = []
    def insertArry(self, value):
        self.arr.append(value)

obj1 = SomeClass()
obj2 = SomeClass()

obj1.insertArry(6)

print("Obj 1", obj1.arr)
print("Obj2 ", obj2.arr)
