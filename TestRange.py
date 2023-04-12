#This code uses range function
#numList = list(range(10))
#print(numList)
#Prints 3 table
#numList = list(range(1, 11))
#for num in numList:
    #print(3*num)


user = int(input("enter a number"))
numList = list(range(1,user))
print(numList)


evenList = list(range(0,user,2))
for num in evenList:
    print(num)
print("Here is a list of even numbers")

