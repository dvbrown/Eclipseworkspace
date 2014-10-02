#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import bibtexparser
import argparse
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

def parseBibtexFile(fileString):
    "Opens a bibtext file and prints a list of dictionaries for reference entries"
    with open(fileString) as bibtex_file:
#===============================================================================
#        bibtex_str = bibtex_file.read()
# 
#    bib_database = bibtexparser.loads(bibtex_str)
#    return bib_database
#===============================================================================
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        return bib_database

def deleteAnote(parsedBibtexFile):
    "Removes the annote field from the bibtex file"
    entries = parsedBibtexFile.entries
    for d in entries:
        if 'annote' in d.keys():
            del d['annote']
        #print d.values()
    return entries

def writebibTex(fileName, fixedBibtex):
    'Open a file and write rows in tab delimited format'
    w = open(fileName, 'w')
    w.write(fixedBibtex.encode('utf8'))
    w.close() 


def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a bibtex flat file containing referencing information
    and removes useless fields like. Emits strings to the standard output""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file containing elements you want to change. 
        The input file should just contain data and no column/ row headers etc''')
    args = parser.parse_args()
    
    fileString = args.inputData
    references = parseBibtexFile(fileString)
    print references.entries
    
    fixedRefs = deleteAnote(references)
    #print fixedRefs
    
    references.entries = fixedRefs
    result = bibtexparser.dumps(references)
    
    writebibTex('output.bib', result)
    
if __name__ == '__main__':
    main()