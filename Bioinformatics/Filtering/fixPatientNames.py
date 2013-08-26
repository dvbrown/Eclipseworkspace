#!/usr/bin/python2.7

#############################################################################################
#Take the somatic mutation names which is the longer code and strip it back to match the gene expression data
#############################################################################################

import sys
#import os
import csv

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
    
    #convert patient IDs of which I have mutation data as a set of names for pattern matching
    mutPatientSet = set(mutPatient[0][1:])
    mutList = [name.strip('-01D-1490-08') for name in mutPatientSet]
    mutList = [name.strip('A') for name in mutList]
    
    print 'patient'+'\t'+'\t'.join(mutList)
    for line in noHeader:
        print '\t'.join(line)
        
if __name__ == '__main__':
    main()
