#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:40:22 2017

@author: Daniel Brown
"""

import argparse

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
parser.add_argument('-p', '--plateType', required=True, help='''The type of plate you have. Valid values are 96 or 384''')
parser.add_argument('-o', '--outputFile', required=True, help='''The name of the output file you want''')
args = parser.parse_args()

