# -*- coding: utf-8 -*-
"""
Created on Wed May 11 13:44:21 2016

@author: u0107775
"""

# Take a spreadsheet with the i5 and i7 sequences listed only and add the sequences of the indexes
# I got the sequences from http://seq.liai.org/204-2/

import sys
import pandas as pd

sampleSheet = sys.argv[1]
nexteraIndexes = sys.argv[2]
output = sys.argv[3]

sampleSheet_df = pd.read_csv(sampleSheet, sep='\t')
nexteraIndexes_df = pd.read_csv(nexteraIndexes, sep='\t')

i7Index = nexteraIndexes_df[['i7 index name', 'i7 base for entry on sample sheet']]
i5Index = nexteraIndexes_df[['i5 index name', 'i5 base for entry on sample sheet']]

print i7Index

df = pd.merge(sampleSheet_df, i7Index, how='inner', left_on='i7', right_on="i7 index name",
        left_index=False, right_index=False, sort=False,
        suffixes=('_x', '_y'), copy=True, indicator=False)
        
df2 = pd.merge(df, i5Index, how='inner', left_on='i5', right_on="i5 index name",
        left_index=False, right_index=False, sort=False,
        suffixes=('_x', '_y'), copy=True, indicator=False)
        
df.to_csv(output, sep='\t')
