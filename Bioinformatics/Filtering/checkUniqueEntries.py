#!/usr/bin/python2.7

#############################################################################################
#Import a tab delimited text file and remove duplicate rows for the perscribed row index index
#############################################################################################

import sys
import csv

def main():
    'Import a tab delimited text file and remove duplicate rows for the perscribed row index index'
    inFile = sys.argv[1]
    columnToCompare = int(sys.argv[2])
    outFile = sys.argv[3]

    data = []
    f = open(inFile, 'U')
    files = csv.reader(f, delimiter='\t')
    for row in files:
        data.append(row)
  
##############################################################################################

#the part of the script that does things
    #for each row of the length of the table
    x = 0
    while x < len(data)-1:
        #Look at the next row and compare the defined entry to the current entry
        #commented out diff = data[i+1][columnToCompare]-data[i][columnToCompare]
        #if the column to compare is identical
        if data[x+1][columnToCompare] == data[x][columnToCompare]:
            print data[x+1][columnToCompare]
            del data[x]
            x += 1
        else:
            x += 1

#############################################################################################

    w = open(outFile, 'w')        
    writer = csv.writer(w ,delimiter="\t")
    for row in data:
        writer.writerow(row)

    f.close()
    w.close() 
    
if __name__ == '__main__':   # this is the boilerplate portion
    main()