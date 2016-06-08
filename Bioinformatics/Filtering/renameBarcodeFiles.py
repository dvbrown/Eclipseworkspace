#!/bin/bash

import csv, aUsefulFunctionsFiltering, os

parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the input''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the output')
    args = parser.parse_args()

#	Read in files
data = aUsefulFunctionsFiltering.readAfile(args.inputData)

files = os.listdir()
#	Turn into a dictionary of the barcode and new filename
dict = {}
for k,v in data:
	dict[k] = v