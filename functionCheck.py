#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:01:24 2018

@author: ajithkumar
"""
"""
#1. Create a function to print hello

def sayHello(firstName,lastName) :
    print ("Hello" + firstName +" " + lastName + ", how are you?")
    return

#2. Invoke the function
sayHello("Shirley"," ")

sayHello("Charlie"," ")

sayHello("Everyone"," ")
"""
"""
def addTwo(var1,var2) :
    sum = var1 + var2 
    return sum

print("Sum of 5 + 5 = " + str(addTwo(5,5)))
"""

# Function definition is here
def printinfo( name, age=16, location="KL" ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   print ("Location: ", location)
   return;

# Now you can call printinfo function
printinfo("miki",50)

printinfo( age=50, name="miki",location="PJ" )

printinfo( name="mini",location="JB" )







