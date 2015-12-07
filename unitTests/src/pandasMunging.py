import pandas as pd
import os
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:50:50 2015

@author: DanBrown
"""
os.chdir("/Users/DanBrown/Code/Python/unitTests/dat")

surveysDF = pd.read_csv("surveys.csv")
#print surveysDF.dtypes # The data types of each object

#print surveysDF.columns
# print surveysDF.tail(5)
# print surveysDF.shape # dimensions of the object
print surveysDF.columns.values
# print pd.unique(surveysDF.sex) # Get unique values from the the species column

# The number of unique plot IDs in the dataframe
#answer = len(pd.unique(surveysDF.plot_id))
#print answer
#print surveysDF.wgt.describe() # Summary statistics on the weight value
#print surveysDF['wgt'].mean()

# The aggreagate style method in pandas
sort = surveysDF.groupby('species')
#print sort.describe()

#sorted2 = surveysDF.groupby(['plot_id', 'sex'])
#print sorted2.mean()

species_list = surveysDF['wgt'].groupby(surveysDF.species).mean()
#print species_list

#species_list.plot(kind='bar')

variable = range(0,5,1)
print 'Here is {1}rd the answer I want for {0}'.format(variable[1], variable[4])

