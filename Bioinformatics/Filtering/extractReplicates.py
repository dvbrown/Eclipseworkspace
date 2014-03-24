#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, itertools, csv
import aUsefulFunctionsFiltering
from locale import str

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the linear data from a 96 well experiment''')
    parser.add_argument('-r', '--replication', required=True, help='''The level of replication of the experiment ie 2 or 3 replicates. CURRENTLY WORKS FOR TRIPLICATE''')
    parser.add_argument('-d', '--direction', required=True, help='''The orientation of the replicates. CURRENTLY ONLY WORKS FOR VERTICAL''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    # Input data
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)
    
    # Extract the well names for replicate 1
    letters1 = ['B', 'C', 'D']
    rep1 = []
    x = 1
    while x < 12:
        x += 1
        y = [letter + str(x) for letter in letters1]
        rep1.append(y)
    
    # Extract replicate names for replicate 2
    letters2 = ['E', 'F', 'G']
    rep2 = []
    x = 1
    while x < 12:
        x += 1
        y = [letter + str(x) for letter in letters2]
        rep2.append(y)    
    
    

    # Make a header
    header = ['wells', 'rep1', 'rep2', 'rep3']
#    print header
    newData = {}
    
######################################## This is the part of the script that does some work ################################################# 
    # Read data into dictionary for later manipulation
    if args.replication == '3':
        for row in data:
            for group in rep1:
                if row[0] in group:
                    group.append(row[1])
###################################################### ###################################################### 
    elif args.replication == '2':
        print "Duplicates ain't implemented yet"
        
    else:
        print "Invalid level of replication"
        
    # Write out to file if one is provided on command line
    if args.outputData == True:
        w = open(args.outputData, 'w')
        writer = csv.writer(w ,delimiter="\t")
        ###################################### Fix the iteration of this
        writer.writerow(zip(wells, plateMap2))
    ######################################
    
    
    for line in rep1:
        print '\t'.join(line)

if __name__ == '__main__':
    main()