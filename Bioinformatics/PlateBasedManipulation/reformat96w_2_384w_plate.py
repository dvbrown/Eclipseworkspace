#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:40:22 2017

@author: Daniel Brown
"""

import argparse, string
import pandas as pd

parser = argparse.ArgumentParser(description="""
    This script can be used to easily convert 96 well plates that have
    been reformatted into 384 well plates for example in the Sous chef PCR cleanup
    It attaches sample labels from Excel speadsheets
    Input is
    Output is
    """)
parser.add_argument('-p', '--plate1', required=True, help='''The first plate that was reformated this is the plate that becomes A1 in the 384 well plate''')
parser.add_argument('-q', '--plate2', required=True, help='''The second plate that was reformated this is the plate that becomes A2 in the 384 well plate''')
parser.add_argument('-r', '--plate3', required=True, help='''The third plate that was reformated this is the plate that becomes B1 in the 384 well plate''')
parser.add_argument('-s', '--plate4', required=True, help='''The fourth plate that was reformated this is the plate that becomes B2 in the 384 well plate''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

def makePlateCoordinates(startLetter, endLetter, startNumber, endNumber):
    'Make the list object with the plate coordinates'
    letters = list(string.ascii_uppercase)
    letters = letters[startLetter:endLetter:2] # change the middle
    number = range(startNumber, endNumber, 2)
    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)
    return wells

def interleavePlates(inputPlate96, coordinate):
    'v'
    # Read in the dataframe
    df_df96_plate = pd.read_csv(inputPlate96)
    df_df96_plate['Coordinate384'] = coordinate
    return df_df96_plate

def main():
    coordinates_p1 = makePlateCoordinates(0,15,1,24)
    coordinates_p2 = makePlateCoordinates(0,15,2,25)
    coordinates_p3 = makePlateCoordinates(1,16,1,24)
    coordinates_p4 = makePlateCoordinates(1,16,2,25)
    p1 = interleavePlates(args.plate1, coordinates_p1)
    p2 = interleavePlates(args.plate2, coordinates_p2)
    p3 = interleavePlates(args.plate3, coordinates_p3)
    p4 = interleavePlates(args.plate4, coordinates_p4)
    df = pd.concat([p1,p2,p3,p4])
    #print(df)
    df.to_csv(args.outputFile)
    index = pd.read_csv('quantifluorLayout.csv')
    print(df.columns)
    print(index.columns)

    dfMerge = pd.merge(index, df, left_on='Coordinate384')
    print(dfMerge)



if __name__ == '__main__':
    main()