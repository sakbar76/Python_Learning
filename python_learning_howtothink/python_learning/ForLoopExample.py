
# For loop example with list/array of strings
for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
    invite = "Hi " + friend + ". Please come to my party!"
    print(invite)


# simple for loop example 2
for i in [0,1,2,3,4]:
    print("value of i: ",i)


# using range keyword in for loop
for i in range (4):
    print("value of i using range keyaowrd: ",i)


# for case where variable not used in loop
for _ in range(5):
    print("This is loop without variable")