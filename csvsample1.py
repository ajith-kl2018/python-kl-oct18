#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 13:15:42 2018

@author: ajithkumar
"""

import csv

myCSVFile = open('data/demo.csv','r')
dataFromFile = csv.reader(myCSVFile)

print(dataFromFile)

for row in dataFromFile:
    print('|'.join(row))
    #for values in row:
    #    print(values)

myCSVFile.close()

