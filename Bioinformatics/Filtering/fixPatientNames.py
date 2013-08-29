#!/usr/bin/python2.7

#############################################################################################
#Take the somatic mutation names which is the longer code and strip it back to match the gene expression data
#############################################################################################

import sys
import os
import csv
import re
os.chdir('/Users/d.brown6/Documents/eQTL/130829_fullData')

def readFileToList(fileName):
    'Reads in a tabular file and extracts the numeric data and column header'
    f = open(fileName, 'U')
    files = csv.reader(f, delimiter='\t')
    data = []
    for row in files:
        data.append(row)
    #get the header row then remove it from data
    return data

#set up script
#os.chdir('/Users/d.brown6/Documents/eQTL/Matrix_eQTL_R/')
mutFile = sys.argv[1]

def main():
    #read in files
    mutPatient = readFileToList(mutFile)
    noHeader = mutPatient[1:][:]
    
    #get rid of TCGA-02-0047-01A-01D-1490-08
    
    #convert patient IDs of which I have mutation data as a set of names for pattern matching
    mutPatientSet = set(mutPatient[0][1:])
    mutList = [re.sub('.-...-....-08','', name) for name in mutPatientSet]
    
    print 'patient'+'\t'+'\t'.join(mutList)
    for line in noHeader:
        print '\t'.join(line)
        
if __name__ == '__main__':
    main()
