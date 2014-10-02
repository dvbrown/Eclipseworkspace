#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import bibtexparser
import argparse 

def parseBibtexFile(fileString):
    "Opens a bibtext file and prints a list of dictionaries for reference entries"
    with open(fileString) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a bibtex flat file containing referencing information
    and removes useless fields like.""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file containing elements you want to change. 
        The input file should just contain data and no column/ row headers etc''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    fileString = args.inputData
    references = parseBibtexFile(fileString)
    print(references.entries)
    
    
    
if __name__ == '__main__':
    main()