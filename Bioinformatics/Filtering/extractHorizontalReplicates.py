#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, itertools, csv
import aUsefulFunctionsFiltering

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the linear data from a 96 well experiment''')
    parser.add_argument('-r', '--replication', required=True, help='''The level of replication of the experiment ie 2 or 3 replicates. CURRENTLY WORKS FOR TRIPLICATE''')
    parser.add_argument('-f', '--fileType', required=True, help='''Whether this is a fluoro plate reader file (no headers)
        or a invasion assay data. Options = fluoro or invasion''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    # Input data. Take out the header if the data is an invasion assay
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)
    if args.fileType == 'invasion':
        header = data[0]
        data = data[1:]
    elif args.fileType == 'fluoro':
        pass
    else:
        print 'This file type is not a valid invasion assay or data from a plate reader'
        
    # Extract the well names for replicate 1. PUT THIS AS A command line argument in the future and collate the 2 replicates into 1
    letters1 = ['B', 'C', 'D']
    # Convert to lower case if the data is invasion assay
    if args.fileType == 'invasion':
        letters1 = ['b', 'c', 'd']          
    rep1 = []
    x = 1
    while x < 13:
        y = [letter + str(x) for letter in letters1]
        rep1.append(y)
        x += 1
    
    # Extract replicate names for replicate 2
    letters2 = ['E', 'F', 'G']
    if args.fileType == 'invasion':
        letters2 = ['e', 'f', 'g']
    rep2 = []
    x = 1
    while x < 13:
    # Using list comprehensions builds the nested list structure that is so useful. Don't use for loops
        y = [letter + str(x) for letter in letters2]
        rep2.append(y)    
        x += 1
    
    # Make a header
    header = ['well1', 'well2', 'well3' ,'rep1', 'rep2', 'rep3']
    print '\t'.join(header)
    
######################################## This is the part of the script that does some work ################################################# 
    # If the data is in triplicate
    if args.replication == '3':
        for row in data:
            wellName = row[0]
            # Strip the file extension from the invasion well names
            if wellName.endswith('.tif'):
                wellName = wellName[:-4]
                
            # Search the well name of the data against the list of lists containing the replicate structure
            for group in rep1:
                if wellName in group:
                    # Append to the replicate structure list
                    group.append(row[1])
            # Repeat for the second group of replicates although one day I will combine this step    
            for group in rep2:
                if wellName in group:
                    group.append(row[1])
###################################################### ###################################################### 
    # Some error messages
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
        ##################################
    
# Print the output to file
    if args.fileType == 'invasion':
        rep1 = rep1[0:4]

    for line in rep1:
        print '\t'.join(line)
    if args.fileType == 'fluoro':
        for line in rep2:
            print '\t'.join(line)
# Good old boiler plate
if __name__ == '__main__':
    main()