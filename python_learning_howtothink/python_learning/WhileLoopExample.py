
# While Loop Example
print("While Loop # 1 Start")
n=6
current_sum=0
i=0

while i<=n:
    current_sum+=i
    i+=1

    # if i==7:
    #     break

    print("Value of i: ",i)
    print ("Current_Sum: ",current_sum)

print ("End of While Loop # 1")


# while loop examples # 2

print ("Start of While Loop # 2")
n = 1027371
while n != 1:
    print(n, end=", ")
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1

print(n, end=".\n")
print("End of While Loop # 2")

# while loop with while boolean expression example
print ("While Loop Example # 3")
total = 0
while True:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "" or response == "-1":
        break
    total += int(response)
    print("The total of the numbers you entered is ", total)