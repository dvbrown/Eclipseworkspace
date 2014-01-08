#!/usr/bin/python

import csv, sys

# The first dataset is gdac.broadinstitute.org_GBM.Merge_transcriptome__agilentg4502a_07_1__unc_edu__Level_3__unc_lowess_normalization_gene_level__data.Level_3.2013121000.0.0/GBM.transcriptome__agilentg4502a_07_1__unc_edu__Level_3__unc_lowess_normalization_gene_level__data.data.txt
# The second dataset is gdac.broadinstitute.org_GBM.Merge_transcriptome__ht_hg_u133a__broad_mit_edu__Level_3__gene_rma__data.Level_3.2013121000.0.0/GBM.transcriptome__ht_hg_u133a__broad_mit_edu__Level_3__gene_rma__data.data.txt

# There are also 2 versions of Agilent data. Better check out what this is

def readFile(filenameString):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter='\t')
    data = []
    for row in inputA:
        data.append(row)
    return data
        
def fixGeneExpressionMatrix(gemDataL3):
    '''Takes a raw level 3 gene expression matrix from firehose and returns something useful for analysis in R
    Takes out line 2 and removes many extraneous codes in the patient name'''
    rawGem = readFile(gemDataL3)
    sampleNames = rawGem[0]
    # Remove line 2
    gem = rawGem[2:]
    # Shorten patient ID
    newNames = []
    for name in sampleNames:
        newName = name[0:12]
        newNames.append(newName)

    print '\t'.join(newNames)
    for line in gem:
        print '\t'.join(line)

# This can be either Agilent or Affymetrix data        
level3DataToFix = fixGeneExpressionMatrix(sys.argv[1])