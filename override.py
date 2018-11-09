#!/usr/bin/python3

class Parent:        # define parent class
   def myMethod(self):
      print ('Calling parent method')

class ChildA(Parent): # define child class
   def myMethod(self):
      print ('Calling child method')


class ChildB(Parent):  # define child class
    name="childB"

c = ChildA()          # instance of child
c.myMethod()         # child calls overridden method

c2 = ChildB()          # instance of child
c2.myMethod()         # child calls overridden method
