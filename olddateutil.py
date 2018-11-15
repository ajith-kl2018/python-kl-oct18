#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 13:10:34 2018

@author: ajithkumar
"""

import datetime

currDate = datetime.date.today()
print (currDate)
print (currDate.year)
print (currDate.month)
print (currDate.day)

#print (currDate.strftime('%d %b, %Y'))

print (currDate.strftime('%A %d %B, %Y'))

print ("Timedelta 15 days : ")
print (currDate + datetime.timedelta(days=15))
print ("Timedelta 15 hours : ")
print (currDate + datetime.timedelta(hours=25))



