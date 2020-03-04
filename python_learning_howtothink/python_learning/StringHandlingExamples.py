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








