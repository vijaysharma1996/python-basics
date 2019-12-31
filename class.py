class Animal(object):
    name = ""

    def eat(self):
        print("%s is eating.." % self.name)
    
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Mammal(Animal):
    hasBackBone = True
    hasHair = True

    def growHair(self):
        print("%s is Growing Hair" % self.name)

cat = Mammal()
dog = Mammal()
snake = Animal()

cat.name = "Shakespear"
dog.name = "Molly"
cat.eat()
cat.growHair()
dog.sleep()