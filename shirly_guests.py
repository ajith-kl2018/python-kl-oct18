#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 13:45:01 2018

@author: ajithkumar
"""

guests = []

guest = "0"

while guest!= " ":
    guest = input("Who is attending party? If no more please put space. ")
    guests.append(guest)
    
guests.sort()

for guest in guests:
    print (guest)

    