#!/usr/bin/python2.7

#############################################################################################
#Import a tab delimited text file and remove the perscribed index
#############################################################################################

import sys
import csv

def main():
    'Takes a tab delimited text file and appends chr to the first column'
    inFile = sys.argv[1]
    columnToDelete = int(sys.argv[2])
    outFile = sys.argv[3]

    data = []
    f = open(inFile, 'U')
    files = csv.reader(f, delimiter='\t')
    for row in files:
        data.append(row)
  
#############################################################################################
#the part of the script that does things

    for row in data:
        del row[columnToDelete]

#############################################################################################

    w = open(outFile, 'w')        
    writer = csv.writer(w ,delimiter="\t")
    for row in data:
        writer.writerow(row)

    f.close()
    w.close() 
    
if __name__ == '__main__':   # this is the boilerplate portion
    main()