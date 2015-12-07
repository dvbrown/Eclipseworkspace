# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:07:51 2015

@author: DanBrown
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/DanBrown/Code/Python/unitTests/dat")
df = pd.read_csv("bouldercreek_09_2013.txt", skiprows=26, sep='\t', header=0)
df = df[1:]

plot_data = df.iloc[1:50, 4]
print plot_data
plt.plot(plot_data, 'o', label='My Data', marker='D')
plt.xlabel('Index')
plt.ylabel('Plot Value')
plt.title('The Plot Value From surveys.csv')
