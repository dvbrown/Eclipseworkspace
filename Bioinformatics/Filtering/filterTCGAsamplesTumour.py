#!/usr/bin/python2.7

import aUsefulFunctionsFiltering, argparse

def main():
    parser = argparse.ArgumentParser(description="""Reads a gene expression matrix from the TCGA and returns only the primary tumour cases""")
    parser.add_argument('-i', '--genomicData', required=True, help='''The file the gene expression matrix''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    gem = aUsefulFunctionsFiltering.readAfile(args.genomicData)
    
    header = gem[0]
    gem = gem[1:]
    gemDict = {}
    
    for entry in gem:
        k = entry[0]
        v = entry[1:]
        gemDict[k] = v
        
    print header
        


if __name__ == '__main__':
    main()        

        
