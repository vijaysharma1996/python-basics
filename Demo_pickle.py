import pickle

class Person(object):
    name = ""
    age = 0

    def __int__(self, name = "Unknown"):
        self.name = name
    def hello(self):
        print("Hello my name is", self.name)

p = Person()
p.name = "Akash"
p.hello()

strfile = "F:/Python/demo.txt"

with open(strfile, "bw") as f:
    pickle.dump(p, f)

print("Pickel landed")

with open(strfile, "br") as f:
    print(pickle.load(f))