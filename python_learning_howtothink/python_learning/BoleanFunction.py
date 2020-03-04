# Boolean function example

## Boolean function with parameters

def is_divisible(x, y):

    print ("Inside the function")
    if x % y == 0:
        return True
    else:
        return False


status=is_divisible(2, 2)
print ("2/2: ",status)

status=is_divisible(3, 2)
print ("3/2: ",status)