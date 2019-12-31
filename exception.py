__author__= "Akash Maniar"

def doSomething(number):
    try:
        x = 5
        y = x/0
        print(y)
    except ZeroDivisionError as e:
        pass
        print("Error occurred is: %s" % e   )
    finally: 
        print("Finally I got to run") 
doSomething(50)
