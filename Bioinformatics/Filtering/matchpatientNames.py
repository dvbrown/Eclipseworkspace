#!/usr/bin/python2.7

#############################################################################################
#Match the patients from which there is somatic mutation data to  the gene expression matrix
#############################################################################################

import sys
import os
import csv
from collections import defaultdict
from test.test_descrtut import defaultdict

def readFileToList(file):
    'Reads in a tabular file and extracts the numeric data and column header'
    f = open(file, 'U')
    files = csv.reader(f, delimiter='\t')
    data = []
    for row in files:
        data.append(row)
    #get the header row then remove it from data
    return data

#set up script
os.chdir('/Users/d.brown6/Documents/eQTL/Matrix_eQTL_R/')
mutFile = sys.argv[1]

#read in files
mutPatient = readFileToList(mutFile)
noHeader = mutPatient[1:][:]

#convert patient IDs of which I have mutation data as a set of names for pattern matching
mutPatientSet = set(mutPatient[0][1:])
mutList = [name.strip('-01D-1490-08') for name in mutPatientSet]
mutList = [name.strip('A') for name in mutList]

print 'patient'+'\t'+'\t'.join(mutList)
for line in noHeader:
    print '\t'.join(line)
