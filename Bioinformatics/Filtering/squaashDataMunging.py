#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, itertools, csv

def readAfile(filenameString):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter=';')
    data = []
    for row in inputA:
        data.append(row)
    fileA.close()
    return data

def writeAfile(fileName, data2Bwritten):
    'Open a file and write rows in tab delimited format'
    w = open(fileName, 'w')        
    writer = csv.writer(w ,delimiter=",")
    for row in data2Bwritten:
        writer.writerow(row)
    w.close()
    
    
    
    
    
    
    
    
def main():
    parser = argparse.ArgumentParser(description="""
    Reads an input file that is output from the imageJ colocalisation plugin 'Squaash'. The data takes all the files put in a directory from
    different imaging fields and combines them into a usable form for analysis in R.
    """)
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the raw data from one field analysed by Squaash.''')
    parser.add_argument('-o', '--outputData', required=False, help='The csv file you get at the end')
    args = parser.parse_args()