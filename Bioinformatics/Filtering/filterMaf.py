#!/usr/bin/python2.7

#############################################################################################
#Filter the mutation call file from TCGA for interesting things
#############################################################################################

import argparse
import csv
import numpy
from numpy.core.numeric import dtype

inFile = '/Users/d.brown6/Documents/public-datasets/firehose/mafDashboard/2013_06_27/test.maf'
outFile = '/Users/d.brown6/Documents/public-datasets/firehose/mafDashboard/2013_06_27/output.maf'
data = []

f = open(inFile, 'U')
files = csv.reader(f, delimiter='\t')
for row in files:
    data.append(row)

#create a matrix object    
matrix = numpy.array(data, dtype='object')
print matrix
    
#w = open(outFile, 'w')        
#writer = csv.writer(w ,delimiter="\t")
#for row in data:
#    writer.writerow(row)

#f.close()
#w.close() 