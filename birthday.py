#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:42:04 2018

@author: ajithkumar
"""

import datetime

birthday = input ("What is your birthday?")

birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y").date()

print ("Your birth month is " + birthdate.strftime('%B')) 

