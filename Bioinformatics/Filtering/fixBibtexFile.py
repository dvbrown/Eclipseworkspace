#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, itertools, csv
import aUsefulFunctionsFiltering 

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a bibtex flat file containing referencing information
    and removes useless fields like.""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file containing elements you want to change. 
        The input file should just contain data and no column/ row headers etc''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    bibtex = aUsefulFunctionsFiltering.readAfile(args.inputData)
    #for line in bibtex:
    entry = [i for i in bibtex]
        
    print bibtex
    
    
    
if __name__ == '__main__':
    main()