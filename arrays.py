#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:34:44 2018

@author: ajithkumar
"""

guests = ['first','second','third']
#print(guests[2])
#print(guests[-1])

#print('First value default :' + guests[0])

guests[0] = 'Steve'

#print('First value is now :' + guests[0])

guests.append('New Guy')

#print('New value is now :' + guests[-1])

#print('2nd Element is :' + guests[1])

#guests.remove('second')
#del guests[1]

#print('2nd Element After remove is :' + guests[1])

#check the index position
#print(guests.index('fourth'))

#for step in range(4):
#for step in range(len(guests)):
#    print(guests[step])
    

#scores = [78,68,88,98,25]
#print(scores[3])
#print(scores[-2])

"""
guests.sort()

for guest in guests:
    print (guest)
    
print ("Done")
"""


scores = [78,68,88,98,25]
scores.sort()

for score in scores:
    print (score)
    
print ("Done")



