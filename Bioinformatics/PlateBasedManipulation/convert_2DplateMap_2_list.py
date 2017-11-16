#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:47:08 2017

@author: u0107775
"""

import argparse, collections

parser = argparse.ArgumentParser(description="""
    This script parsers the plate layout from cell sorting in 2D format.
    It then creates a list based csv file with the well position, sample name and cell number as columns.
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The file with the sort template in 2D format''')
parser.add_argument('-p', '--plateType', required=True, help='''The type of plate you have. Currently valid values are 96 but one day I will make 384 well''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

fileInput = args.inputFile

def read2DplateMap(inputFile):
    'Read in the xth and yth line of the file which contains sample name and cell number respecitively'
    fileA = open(inputFile, 'U')
    inputA = csv.reader(fileA, delimiter=",")
    # Read the whole file into a list
    wholeFile = []
    print wholeFile
    # Need to find a way to loop through the nth line of a file
    for line in inputA:
        sample.append(line[0:])

    # Initialise a list for sample name and a different list for cell number
    sampleName = []
    for line in wholeFile:
        wholeFile.append(line[1::4]) # Change this number depending on which line is the sample number
    cellNumber = []
    for line in wholeFile:
        wholeFile.append(line[1::4]) # Change this number depending on which line is the sample number
    return sampleName, cellNumber


# Once I have a list of sample names and a list of cell number zip them together in an ordered dict
    def zipSample_cellNumber_together(sampleName, cellNumber):

def main():
    read2DplateMap(fileInput)

if __name__ == '__main__':
    main()