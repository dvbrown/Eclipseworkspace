#!/usr/bin/python

# The data originally came from broad firehose => firehose_get -b -o MAF Agilent U133A clinical stddata 2013_12_10 GBM
# This script will take a clinical report file and 2 gene expression files
# Gene expression file 1 = Agilent. File 2 = Affymetrix

# Remember there is a version 1 and version 2. They are actually identical
# gdac.broadinstitute.org_GBM.Merge_Clinical.Level_1.2013121000.0.0/GBM.merged_only_clin_data.txt
# gdac.broadinstitute.org_GBM.Merge_Clinical.Level_1.2013121000.0.0 2/GBM.merged_only_clin_data.txt

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
def main():     
    clinicalData = readFile(sys.argv[1])
    fieldnames = ('patient.daystodeath', 'patient.ageatinitialpathologicdiagnosis', 
                    'patient.drugs.drug-2.drugname',
                    'patient.drugs.drug-2.therapytypes.therapytype', 'patient.drugs.drug-3.regimenindication', 
                    'patient.followups.followup.daystotumorrecurrence','patient.followups.followup.karnofskyperformancescore', 
                    'patient.followups.followup.vitalstatus', 'patient.gender',
                    'patient.histologicaltype', 'patient.race')
    
    patientNames = clinicalData['patient.bcrpatientbarcode']
    filteredData = {k: clinicalData[k] for k in fieldnames}
    
    # Fix patient Names to agree with gene expression table
    newNames = []
    for name in patientNames:
        name = name.upper()
        newNames.append(name)
    # Write out file to disk
    print '\t'.join(newNames)
            
    for k, v in filteredData.items():
        print k + '\t' + '\t'.join(v)

if __name__ == '__main__':
    main()

