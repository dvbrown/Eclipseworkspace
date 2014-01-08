#!/usr/bin/python

# The data originally came from broad firehose => firehose_get -b -o MAF Agilent U133A clinical stddata 2013_12_10 GBM
# This script will take a clinical report file and 2 gene expression files
# Gene expression file 1 = Agilent. File 2 = Affymetrix

# Remember there is a version 1 and version 2
# gdac.broadinstitute.org_GBM.Merge_Clinical.Level_1.2013121000.0.0/GBM.clin.merged.txt
# gdac.broadinstitute.org_GBM.Merge_Clinical.Level_1.2013121000.0.0 2/GBM.clin.merged.txt

import csv, sys

def readFile(filenameString):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter='\t')
    data = []
    for row in inputA:
        data.append(row)
    
    # Now make a dictionary where the rowname is the key
    result = {}
    for entry in data:
        key = entry[0]
        values = entry[1:(len(data)+1)]
        result[key] = values
    return result


# Embed this in a main function when finished
     
clinicalData = readFile(sys.argv[1])
usefulFields = ('patient.bcrpatientbarcode', 'patient.daystodeath', 'patient.ageatinitialpathologicdiagnosis', 
                'patient.drugs.drug-2.drugname',
                'patient.drugs.drug-2.therapytypes.therapytype', 'patient.drugs.drug-3.regimenindication', 
                'patient.followups.followup.daystotumorrecurrence','patient.followups.followup.karnofskyperformancescore', 
                'patient.followups.followup.vitalstatus', 'patient.gender',
                'patient.histologicaltype', 'patient.race')

filteredData = {k: clinicalData[k] for k in usefulFields}
