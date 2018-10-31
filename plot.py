#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:50:25 2018

@author: ajithkumar
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,1,300)
for w in range(2, 6, 2):
	plt.plot(x, np.sin(np.pi*x)*np.sin(2*w*np.pi*x))


