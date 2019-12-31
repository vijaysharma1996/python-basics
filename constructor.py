class Animal(object):
    name = "Not named"

    def __init__(self):
        print("Animal Constructed") 

class Reptile(Animal):
    hasScales = True

    def __init__(self):
        super().__init__() #Must init the super
        print("Reptile constructed")

class Mammal(Animal):
    hasHair = True

    def __init__(self):
        super().__init__()
        self.hasBackBone = True
        print("Mammal Constructed")

class Dragon(Reptile, Mammal):
    hasWings = True

    def __init__(self):
        # This is called as the variable shadowing as parent variable is shadowed
        # by the child variable
        
        self.hasHair = False 
        super().__init__() #Must init the super 
        print("Dragon Constructed")

    def __del__(self):
        print(self.__class__.__name__ + " destroyed")

myDragon1 = Dragon()

print(myDragon1.hasHair)
# print(myDragon1.hasBackBone)