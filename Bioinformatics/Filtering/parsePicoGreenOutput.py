#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse, aUsefulFunctionsFiltering, itertools, string

parser = argparse.ArgumentParser(description="""
    This script parsers output from the Picogreen software.
    Input is a csv file converted file from the Pciogreen reader.
    Output is a column based list of concentrations wih well coordinates
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The file that you got from the Picogreen reader. This should be a csv file.''')
parser.add_argument('-p', '--plateType', required=True, help='''The type of plate you have. Valid values are 96 or 384''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

# Sanity check plate type
plate = args.plateType

def parsePicogreenOutput96(picoGreenOutput):
    'Reads the output of the Picogreen assay in .txt format and removes all the unecessary parts of the file'
    # Read in the input file. First test if it is a csv
    if picoGreenOutput[-4:] != '.txt':
        print 'Your input file is not in tab format. It is probably in .xls and you should convert to .tab first'

    dat = aUsefulFunctionsFiltering.readAfile(args.inputFile)
    dat = dat[13:21]

    # Cut out the first and last columns
    plateMap = [row[2:13] for row in dat]
    # Change the commas to points
    noCommas = []
    for row in plateMap:
        noCommas.append([i.replace(",", ".") for i in row])
    return noCommas

def parsePicogreenOutput384(picoGreenOutput):
    'Reads the output of the Picogreen assay in .txt format and removes all the unecessary parts of the file'
    # Read in the input file. First test if it is a csv
    if picoGreenOutput[-4:] != '.txt':
        print 'Your input file is not in tab format. It is probably in .xls and you should convert to .tab first'
    dat = aUsefulFunctionsFiltering.readAfile(args.inputFile)
    dat = dat[13:]
    # Cut out the first and last columns
    plateMap = [row[2:25] for row in dat]
    # Change the commas to points
    noCommas = []
    for row in plateMap:
        noCommas.append([i.replace(",", ".") for i in row])
    return noCommas

def plate2columnConvert96(plateData):
    'Converts the plate output of parsePicogreenOutput and turns it into a column based format'
    plateMap = list(itertools.chain.from_iterable(plateData))
    # Write in the well names
    letters = list(string.ascii_uppercase)
    letters = letters[0:8]
    number = range(2, 13)
    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)
    # Zip the data and well names together
    outTuple = zip(wells, plateMap)
    outList = [list(row) for row in outTuple]

    # Print the output to the user
    for well, gene in zip(wells, plateMap):
        print well + '\t' + gene
    return outList

def plate2columnConvert384(plateData):
    'Converts the plate output of parsePicogreenOutput and turns it into a column based format'
    plateMap = list(itertools.chain.from_iterable(plateData))
    # Write in the well names
    letters = list(string.ascii_uppercase)
    letters = letters[0:16]
    number = range(2, 26)
    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)
    # Zip the data and well names together
    outTuple = zip(wells, plateMap)
    outList = [list(row) for row in outTuple]

    # Print the output to the user
    for well, gene in zip(wells, plateMap):
        print well + '\t' + gene
    return outList

def main():
    if plate == "96":
        plateData = parsePicogreenOutput96(args.inputFile)
        columnData= plate2columnConvert96(plateData)
        aUsefulFunctionsFiltering.writeAfile(args.outputFile, columnData)

    elif plate == "384":
        plateData = parsePicogreenOutput384(args.inputFile)
        columnData= plate2columnConvert384(plateData)
        aUsefulFunctionsFiltering.writeAfile(args.outputFile, columnData)
    else:
        print "You have not entered a valid plate type. Type 96 or 384"

if __name__ == '__main__':
    main()
