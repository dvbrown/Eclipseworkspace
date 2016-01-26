# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:02:20 2015

@author: DanBrown
"""

import pandas as pd
import os

os.chdir("/Users/DanBrown/Code/Python/unitTests/dat")
df = pd.read_csv("surveys.csv")
print df.columns.values

print df.year == df['year']