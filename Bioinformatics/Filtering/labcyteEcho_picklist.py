#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:37:40 2017

@author: Daniel Brown
"""

import aUsefulFunctionsFiltering, argparse
import pandas as pd

dnaPickFile = "../pickList_DNA.csv"
waterPickFile = "../pickList_Water.csv"

parser = argparse.ArgumentParser(description="""
    This script calculates the DNA picklist and water picklist for the Labcyte Echo
    Input is the column based representation of Picogreen assay
    Output is the picklists for the labcyte Echo
    """)
parser.add_argument('-i', '--inputFile', required=True, help='''The column based file that was munged by the parsePicogreenOutput script''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

# Read in the DNA concentration file
def readDNAconcentration_2_dataframe(dnaConcFile):
     df_DNA_concentration = pd.read_table(dnaConcFile, sep='\t', header=None, index_col=0)
     # Insert the plate name
     rowName= list(df_DNA_concentration.index)
     newRowNames = ['Plate1_' + i for i in rowName]
     df_DNA_concentration.index = (newRowNames)
     return df_DNA_concentration



# Calculate the amount of DNA to add in the Labcyte Echo
def calculateLabcyte_input(df_DNA_concentration):
    dnaPickList = pd.read_table(dnaPickFile, sep=',', header=0, index_col=1)

    # Join the dna dataframe with the Picogreen concentrations
    joined = pd.merge(dnaPickList, df_DNA_concentration, how='inner', left_on="Sample ID",
         right_index=True, sort=False, copy=True)
    return joined



# Write out the picklist for the DNA and for the water
def generatePicklist():
    pass

def main():
    df = readDNAconcentration_2_dataframe(args.inputFile)
    print calculateLabcyte_input(df).head()

if __name__ == '__main__':
    main()