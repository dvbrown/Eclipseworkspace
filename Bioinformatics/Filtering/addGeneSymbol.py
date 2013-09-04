#!/usr/bin/python2.7

#############################################################################################
#Take the somatic mutation names which is the longer code and strip it back to match the gene expression data
#############################################################################################

import csv
import os
os.chdir('/Users/d.brown6/Documents/FredCSC/reformattedFiles/symbolConversion')

def readFileToList(fileName):
    'Reads in a tabular file and extracts the numeric data and column header'
    f = open(fileName, 'U')
    files = csv.reader(f, delimiter='\t')
    data = []
    for row in files:
        data.append(row)
    #get the header row then remove it from data
    return data

geneExp1 = readFileToList('130830_gseaExpression.gct')
geneExp = geneExp1[3:]

symbols1 = readFileToList('130830_convertgct.txt')
symbols = symbols1[1:]

for gene in symbols:
    enterezID = gene[0]
    geneSymbol = gene[1]
    for entry in geneExp:
        if entry[0] == enterezID:
            entry[1] = geneSymbol
#        else:
#            entry[1] = 'NA'

for line in geneExp1[0:3]:
    print '\t'.join(line)            
for line in geneExp:
    print '\t'.join(line)
