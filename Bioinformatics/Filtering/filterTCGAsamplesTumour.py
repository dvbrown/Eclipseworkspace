#!/usr/bin/python2.7

import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description="""Reads a gene expression matrix from the TCGA and returns only the primary tumour cases""")
    parser.add_argument('-i', '--genomicData', required=True, help='''The file the gene expression matrix''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    gem = pd.read_csv(args.genomicData, sep='\t')
    # Use this syntax to extract columns
    print gem.loc[:,['sample1', 'sample2']]
    
    gem.pd.to_csv(sep="\t")
    
    
if __name__ == '__main__':
    main()
    
   

        
