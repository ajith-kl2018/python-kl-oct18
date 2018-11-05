#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:41:35 2018

@author: ajithkumar
"""

guests = []
name = "  "
  
while name != "DONE" :
    name = input("Enter guest name (enter DONE if no more names) : ")
    if name!= "DONE" :
        guests.append(name) 

guests.sort() 
for guest in guests :
     print(guest)
