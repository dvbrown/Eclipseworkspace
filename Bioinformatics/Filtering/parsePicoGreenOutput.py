# -*- coding: utf-8 -*-

import argparse, aUsefulFunctionsFiltering, itertools, string

parser = argparse.ArgumentParser(description="""
    This script parsers output from the Picogreen software.
    Input is a csv file converted file from the Pciogreen reader.
    Output is a column based list of concentrations wih well coordinates
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The file that you got from the Picogreen reader. This should be a csv file.''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

def parsePicogreenOutput(picoGreenOutput):
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

def plate2columnConvert(plateData):
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

def main():
    plateData = parsePicogreenOutput(args.inputFile)
    columnData= plate2columnConvert(plateData)
    aUsefulFunctionsFiltering.writeAfile(args.outputFile, columnData)

if __name__ == '__main__':
    main()