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
geneFile = sys.argv[2]

#read in files
mutPatient = readFileToList(mutFile)

genePatient = readFileToList(geneFile)
geneList = genePatient[0]

#convert patient IDs of which I have mutation data as a set of names for pattern matching
mutPatientSet = set(mutPatient[0][1:])
mutList = [name.strip('-01D-1490-08') for name in mutPatientSet]
mutList = [name.strip('A') for name in mutList]
print mutList

##create a default Dict for the gene expression data. The patient names as keys and their gene expression as values
#geneExprDict = defaultdict(set)
#geneExprDict.keys(geneList)
#for entry in genePatient:
#    p = entry
#
#ind = []
#for patient in mutList:
#    if patient in geneList:
#        ind.append(geneList.index(patient))
#
#output = genePatient[1,2][:]
#print output