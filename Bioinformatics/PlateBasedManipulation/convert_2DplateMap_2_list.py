#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:47:08 2017

@author: u0107775
"""

import argparse, csv, string
import pandas as pd

parser = argparse.ArgumentParser(description="""
    This script parsers the plate layout from cell sorting in 2D format.
    It then creates a list based csv file with the well position, sample name and cell number as columns.
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The file with the sort template in 2D format''')
parser.add_argument('-p', '--plateType', required=False, help='''The type of plate you have. Currently valid values are 96 but one day I will make 384 well''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

fileInput = args.inputFile
outFileName = args.outputFile

def readFile(inputFile):
    'Read input file'
    fileA = open(inputFile, 'U')
    inputA = csv.reader(fileA, delimiter='\t')
    # Read the whole file into a list
    wholeFile = []
    for line in inputA:
        wholeFile.append(line)
    # Remove the header
    wholeFile = wholeFile[1:]
    return wholeFile

def read2DplateMap(plateMapList, int_sampleNameSkip=4, int_cellNumberSkip=4):
    'Take the list of the plate map and return the sample name and cell number separately'
    # Extract the sample name and cell number from the list
    stop = len(plateMapList)
    sampleName = plateMapList[2:stop:int_sampleNameSkip]
    cellNumber = plateMapList[3:stop:int_cellNumberSkip]
    # Remove the empty 1st element of each list
    sampleName = [i[1:] for i in sampleName]
    cellNumber = [i[1:] for i in cellNumber]
    return sampleName, cellNumber

def makePlateCoordinates():
    'Make the list object with the plate coordinates'
    letters = list(string.ascii_uppercase)
    letters = letters[0:8]
    number = range(1, 13)
    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)
    return wells

# Once I have a list of sample names and a list of cell number zip them together in an ordered dict
def zipSample_cellNumber_together(platecoordinates, sampleName, cellNumber):
    'What this finction does'
#    ordDict = collections.OrderedDict()
#    ordDict['Well'] = ['Sample', 'Cell_number']
    # Flatten the sample name and cell number list
    flatSample = [item for sublist in sampleName for item in sublist]
    flatCellnumber = [item for sublist in cellNumber for item in sublist]
    df = pd.DataFrame(
    {'Coordinate': platecoordinates,
     'Identity': flatSample,
     'Number': flatCellnumber
    })
    return df

def main():
    plateMap = readFile(fileInput)
    sample, cellNo = read2DplateMap(plateMap, 4, 4)
    coordinates = makePlateCoordinates()
    dataFrame = zipSample_cellNumber_together(coordinates, sample, cellNo)
    print(dataFrame)
    dataFrame.to_csv(outFileName)

if __name__ == '__main__':
    main()