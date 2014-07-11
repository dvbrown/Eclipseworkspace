#!/usr/bin/python2.7

import aUsefulFunctionsFiltering, argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="""Reads a gene expression matrix from the TCGA and returns only the primary tumour cases""")
    parser.add_argument('-i', '--genomicData', required=True, help='''The file the gene expression matrix''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    gem = np.loadtxt(args.genomicData, delimiter='\t', skiprows=2)
    print gem
    
    
if __name__ == 'main':
    main()
    
   

        
