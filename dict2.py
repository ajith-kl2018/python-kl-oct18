#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:25:05 2018

@author: ajithkumar
"""

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
       counts[name] = 1
    else :
        counts[name] = counts[name] + 1
        

print(counts)

print(counts.get('csev',0))
        
        