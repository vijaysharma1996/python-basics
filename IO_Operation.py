# name, phone = input("Enter name and phone number: ").split()
# print("The name and phone number are ", name, phone)

try:
    x, y = [int(x) for x in input("Enter two value: ").split()]
except ValueError:
    print("Value you have entered is either not according to ")
print("X and Y are :-",x,y)