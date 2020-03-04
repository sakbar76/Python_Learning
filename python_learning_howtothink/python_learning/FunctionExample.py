# Functions example in python
#

def myFunction ():
    print("hello world inside the function")

    for i in range (4):
        print("loop inside the function: ",i)


def myFunctionReturns(a,b):
    c =a +b
    return c


## calling the function
a=10
b=20

myFunction()
d=myFunctionReturns(a,b)

print ("Value of d after function call: ",d)