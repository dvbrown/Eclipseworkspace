#!/usr/bin/python2.7

import argparse
import pandas as pd

def main():
    '''Takes a gct file formatted for GSEA and returns only the primary tumours
     as a gene expression matrix'''
    parser = argparse.ArgumentParser(description="""Reads a gene expression matrix from the TCGA and returns only the primary tumour cases""")
    parser.add_argument('-i', '--genomicData', required=True, help='''The file the gene expression matrix''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    gem = pd.read_csv(args.genomicData, sep='\t', skiprows=2, index_col=0)
    
    # reguar expression to extract primary tumour farom patients.
    # last 2 strings will be '01'
    header = list(gem.columns.values)
    
    primaryTumour = []
    for p in header:
        tissue = p[12:15]
        if tissue == '-01':
            primaryTumour.append(p)
            
    # Use this syntax to extract columns
    result = gem.loc[:,primaryTumour]
    result.to_csv(args.outputData, sep='\t')
    
    
if __name__ == '__main__':
    main()
    
   

        
