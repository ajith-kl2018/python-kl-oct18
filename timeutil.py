#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:07:43 2018

@author: ajithkumar
"""

import datetime

currentTime = datetime.datetime.now()

print (currentTime)
print (currentTime.hour)
print (currentTime.minute)
print (currentTime.second)

print (datetime.datetime.strftime(currentTime,'%H:%M'))

print (datetime.datetime.strftime(currentTime,'%I:%M %p'))




