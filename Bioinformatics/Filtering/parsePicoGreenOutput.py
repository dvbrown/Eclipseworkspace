# -*- coding: utf-8 -*-

import argparse, aUsefulFunctionsFiltering

parser = argparse.ArgumentParser(description="""
    This script parsers output from the Picogreen software.
    Input is a csv file converted file from the Pciogreen reader.
    Output is a column based list of concentrations wih well coordinates
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The file that you got from the Picogreen reader. This should be a csv file.''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

# Read in the input file. First test if it is a csv
if args.inputFile[-4:] != '.txt':
    print 'Your input file is not in tab format. It is probably in .xls and you should convert to .tab first'

dat = aUsefulFunctionsFiltering.readAfile(args.inputFile)


dat = dat[13:21]


# Cut out the first and last columns
out = [row[2:13] for row in dat]
#for row in dat:
#    for i in row[2:13]:
#        print i # Need to fix this with some checking


#aUsefulFunctionsFiltering.writeAfile(args.outputFile, out)