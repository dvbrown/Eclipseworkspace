#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, itertools, csv
import aUsefulFunctionsFiltering 

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the linear data from a 96 well experiment''')
    parser.add_argument('-r', '--replication', required=True, help='''The level of replication of the experiment ie 2 or 3 replicates. CURRENTLY WORKS FOR TRIPLICATE''')
    parser.add_argument('-d', '--direction', required=True, help='''The orientation of the replicates. CURRENTLY ONLY WORKS FOR VERTICAL''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)

    # Make a header
    header = ['wells', 'rep1', 'rep2', 'rep3']
    print header

    if args.replication == 3:
        for row in data

    # Write out to file if one is provided on command line
    if args.outputData == True:
        w = open(args.outputData, 'w')
        writer = csv.writer(w ,delimiter="\t")
        ###################################### Fix the iteration of this
        writer.writerow(zip(wells, plateMap2))
    ######################################
    
    
    for row in data:
        print row

if __name__ == '__main__':
    main()