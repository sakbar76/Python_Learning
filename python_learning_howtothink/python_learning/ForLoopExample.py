
# For loop example # 1 --- with list/array of strings
print ("Loop Example 1")
for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
    invite = "Hi " + friend + ". Please come to my party!"
    print(invite)


# for loop example 2 --- loop counter in list
print ("Loop Example 2")
for i in [0,1,2,3,4]:
    print("value of i: ",i)


# for loop examples # 3 -- using range keyword in for loop
print ("Loop Example 3")
for i in range (4):
    print("value of i using range keyaowrd: ",i)


# for loop example # 4 -- case where variable not used in loop
print ("Loop Example 4")
for _ in range(5):
    print("This is loop without variable")


# for loop example 5 --- with instance of list/object
print ("Loop Example 5")
numbers = [5, 6, 32, 21, 9]
running_total = 0
for number in numbers:
    running_total = running_total + number
    print(running_total)

# for loop example 6 --- using range keyworkd
print ("Loop Example 6")
for x in range(13):
    print(x, "\t", 2**x)


# for loop example 7 --- range keyword with starting loop variable value
print ("Loop Example 7")
for x in range (1,7):
    print(2 * x, end=" ")
print ()

# for loop example 8 --- continue example in for loop
print ("Loop Example 8")
for i in [12,16,17,24,29,30]:
    if i % 2 == 1:
        continue
    print (i)
print("Done with the loop in example # 8....")

