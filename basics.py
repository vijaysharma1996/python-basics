list = [1,2,9,"Cat", "Mango"]
print("Cat counts are: ", list.count("Cat"))
print("Cat counts are: ", list.append("Rat"))
print(list);
list.reverse();
print(list);

ages = {"Bryan": 40, "Heather": 22}
print(ages);
print(ages.keys())
print(ages.values())
ages["Bryan"] = 44
print(ages.items())

ages = {"Bryan": 40, "Heather": 22}
for name, age in ages.items():
    print(" %s is %d years old" % (name, age))

