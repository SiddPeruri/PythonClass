from math import sqrt

user=input("Do you want to calculate a, b, or c?")
if user == 'c':
    a = int(input("what is the length of side a"))
    b = int(input("what is the length of side b"))
    c = sqrt(a * a + b * b)
    print(c)
if user == 'b':
    c = int(input("What is the length of side c"))
    a = int(input("What is the length of side a"))
    b = sqrt(c * c - a * a)
    print(b)
if user == 'a':
    c = int(input("What is the length of side c"))
    b = int(input("What is the length of side b"))
    a = sqrt(c * c - b * b)
    print(a)

