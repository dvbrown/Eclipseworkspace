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

def main():
    coordinates = makePlateCoordinates()
    print coordinates
    df96_1 = args.plate1
    df96_2 = args.plate2
    df96_3 = args.plate3
    df96_4 = args.plate4


if __name__ == '__main__':
    main()