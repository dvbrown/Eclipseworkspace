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

def makePlateCoordinates():
    'Make the list object with the plate coordinates'
    letters = list(string.ascii_uppercase)
    letters = letters[0:16]
    number = range(1, 25)
    wells = []
    for letter in letters:
        for num in number:
            x = letter + str(num)
            wells.append(x)
    return wells

def interleavePlates(plate1, plate2, plate3, plate4, coordinateWell):
    ''
    plt1_newcoordinate = coordinateWell[0:384:2]
    plt1_newcoordinate = plt1_newcoordinate[0:192:12]
    return plt1_newcoordinate

def main():
    coordinates = makePlateCoordinates()
    df96_1 = pd.read_csv(args.plate1)
    df96_2 = pd.read_csv(args.plate2)
    df96_3 = pd.read_csv(args.plate3)
    df96_4 = pd.read_csv(args.plate4)
    interleavePlates(df96_1, df96_2, df96_3, df96_4, coordinates)


if __name__ == '__main__':
    main()