#!/usr/bin/python2.7

#############################################################################################
#Take the somatic mutation names which is the longer code and strip it back to match the gene expression data
#############################################################################################

import argparse
import csv
#import os
import re
#os.chdir('/Users/d.brown6/Documents/eQTL/130829_fullData')

def readFileToList(fileName):
    'Reads in a tabular file and extracts the numeric data and column header'
    f = open(fileName, 'U')
    files = csv.reader(f, delimiter='\t')
    data = []
    for row in files:
        data.append(row)
    #get the header row then remove it from data
    return data

def main():
    parser = argparse.ArgumentParser(description="Take the somatic mutation names which is the longer code and strip it back to match the gene expression data")
    parser.add_argument('-m', '--mutationfile', required=False, help='a snp converted mutation file from the TCGA')
    parser.add_argument('-g', '--hiseqGeneFile', required=False, help='gene expression matrix from hiseq RNA-seq')
    args = parser.parse_args()

#read in file depending on option at command line 
    if args.mutationfile:
        mutPatient = readFileToList(args.mutationfile)
    elif args.hiseqGeneFile:
        mutPatient = readFileToList(args.hiseqGeneFile)
        
    noHeader = mutPatient[1:][:]
    
    #convert patient IDs of which I have mutation data as a set of names for pattern matching
    mutPatientSet = set(mutPatient[0][1:])
    if args.mutationfile:  
        mutList = [re.sub('.-...-....-08','', name) for name in mutPatientSet]
    elif args.hiseqGeneFile:
        mutList = [re.sub('.-...-....-01','', name) for name in mutPatientSet]
    
    print 'patient'+'\t'+'\t'.join(mutList)
    for line in noHeader:
        print '\t'.join(line)
        
if __name__ == '__main__':
    main()
