# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:41:16 2020

@author: Hasee
"""

import math
r = 3.0
A = math.pi*r**2
print('Area of the circle is: ',A)

def circleArea(r):
    return math.pi*r**2

def squareArea(a):
    return a**2

def rectangleArea(a,b):
    return a*b

def triangleArea(b,h):
    return 0.5*b*h

goAgain = 'y'

while (goAgain == 'y'):
    print("Which shape's area do you want to calculate?")
    print("\n1.Circle")
    print("\n2.Square")
    print("\n3.Rectangle")
    print("\n4.Triangle")

    choice = input("\nEnter the number of your choice:")

    if (choice == '1'):
        r = float(input("\nEnter the radius of the circle"))
        print("\nArea of the cicle is:", circleArea(r))
        
    if (choice == '2'):
        a = float(input("\nEnter the side length of the square"))
        print("\nArea of the square is:", squareArea(r))
        
    if (choice == '3'):
        a = float(input("\nEnter the first side of the rectangle"))
        b = float(input("\nEnter the second side of the rectangle"))
        print("\nArea of the rectangle is:", rectangleArea(a,b))
    
    if (choice == '4'):
        b = float(input("\nEnter the base of the triangle"))
        h = float(input("\nEnter the height of the triangle"))
        print("\nArea of the triangle is:", triangleArea(b,h))
        
    goAgain = input("\nWould you like to ran again (y/n)")
    
print("\nThank you for using our program")