#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:36:08 2018

@author: ajithkumar
"""

fileName = "Sample.txt"
accessMode = "w"

myFile = open(fileName,accessMode)
myFile.write("Hi!!,\n")
myFile.write("How are you?")
myFile.close()

