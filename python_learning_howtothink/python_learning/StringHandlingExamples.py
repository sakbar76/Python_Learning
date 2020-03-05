#################### String Handling Examples #############################

## string value
name="Shakeel Akbar Muhammad Akbar"

## print length of the string
print (">>> Length of the String is: ",len(name))


## find text shakeel in string
if name.find("Shakeel") >= 0:
    print(">>> Found 'shakeel' in the string")
else:
    print(">>> Not found 'shakeel' in the string")

# print at specific index
print(name[0])

# print specific range
print(name[0:7])

# print string in reverse order
print(name[::-1])

# print and check for substring in startswith
print (name.startswith("Shakeel"))

# print and check for substring in endswith
print (name.endswith("Akbar"))

# Split the string
split_string=name.split(" ")
print (split_string)

# enumerate string to a list
fruit="banana"
list (enumerate(fruit))
print (fruit)







