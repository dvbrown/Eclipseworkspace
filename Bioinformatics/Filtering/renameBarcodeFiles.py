#!/bin/bash

import aUsefulFunctionsFiltering
import argparse, os

parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
parser.add_argument('-i', '--inputData', required=True, help='''The file that is the input''')
parser.add_argument('-g', '--gcCode', required=True, help='''The GC code of your run''')
parser.add_argument('-o', '--outputData', required=False, help='The file you get at the output')
args = parser.parse_args()

def main():
#	Read in files from the command line
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)
    
    # Get the filenames from the current directory
    files = os.listdir('.')
    
    #	Turn into a dictionary of the barcode and new filename
    dic = {}
    for row in data:
        dic[row[0]] = row[1]
     
    #   Match filenames
    for k in dic.keys():
        for f in files:
            if k in f:
                # Write the new filename using the value of the barcode dictionary
                newName = dic[k] + '_' + f
                print "old file name = {0} \t new file name = {1} \n".format(f, newName)
                # Make a new file by copying the name of the old file + new information from dictionary
                os.system('cp {0} {1}'.format(f, newName))

if __name__ == '__main__':
    main()
