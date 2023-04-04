# python file for strings
name = input("Enter your name: ")
#print(name[0])
#print(name[1])
#print(name[3])
#print(len(name))
counter = 0
while counter < len(name):
    print(name[counter])
    counter=counter + 1


# join function
strList = ["Hello", name]
#mylist = [1, 4, 6, 9]
#print(f"Hello{name}")
toPrint = " ".join(strList)
print(toPrint)