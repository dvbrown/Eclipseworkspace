#!/usr/bin/python2.7

#############################################################################################
#Import a bed or gtf file or soforth and append the pesky chr to make it compatible with hg19
#############################################################################################

import sys
import csv
import collections

def main():
    'Takes a tab delimited text file and appends chr to the first column'
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    data = []
    f = open(inFile, 'U')
    files = csv.reader(f, delimiter='\t')
    for row in files:
        data.append(row)
############################################################################################    
#The part of the program that does stuff goes here
############################################################################################    
    geneSymbol = []
    for row in data:
        geneSymbol.append(row[15])
    cnt = collections.Counter()
    
    for symbol in geneSymbol:
        cnt[symbol] += 1
    print cnt


#write out the file
    w = open(outFile, 'w')        
    writer = csv.writer(w ,delimiter="\t")
    for row in data:
        writer.writerow(row)

    f.close()
    w.close() 
    
if __name__ == '__main__':   # this is the boilerplate portion
    main()