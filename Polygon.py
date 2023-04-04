# program to draw polygon using turtle
from turtle import *

from pip._internal.vcs import git


def polygon(length, sides):
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)

s = int(input("Enter number of sides: "))
l = int(input("Enter number of sides: "))
polygon(s,l)
done()






