#!/bin/bash

import aUsefulFunctionsFiltering
import argparse, os

parser = argparse.ArgumentParser(description="""
Input is a directory with filenames corresponding to sequencing indexes.
You also need a tab delimited file with the sequencing indexes in one column and the actual name of the sample in other column.
The output is renamed files. The original file is NOT overwritten.
""")
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
