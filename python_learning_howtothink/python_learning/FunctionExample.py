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

## calling function with no return value
myFunction()

print ("value of a: ",a)
print ("value of b: ",b)

## calling fruitful function
d=myFunctionReturns(a,b)

print ("Value of d after function call: ",d)

