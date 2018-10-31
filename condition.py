#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:20:08 2018

@author: ajithkumar
"""

answer = input("Would you like an Express Shipping? (Yes or No) ").lower()
shippingSelected = False

if answer == "yes" : 
    print("That will be an extra 10$")
    shippingSelected = True
else :
    print("Standard Shipping selected..")


if(shippingSelected) :
    print("Thank you for selecting Express shipping !!")
