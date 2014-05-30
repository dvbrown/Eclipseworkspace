#!/usr/bin/python2.7

import aUsefulFunctionsFiltering, argparse

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a 96 well plate and transposes it 
        to yield the column letter.""")
    parser.add_argument('-i', '--genomicData', required=True, help='''The file containing elements you want to change. 
        The input file should just contain data and no column/ row headers etc''')
    parser.add_argument('-m', '--diseaseMap', required=False, help='The map that describes disease codes')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    rawTable = aUsefulFunctionsFiltering.readAfile(args.genomicData)
    diseaseCode = aUsefulFunctionsFiltering.readAfile(args.diseaseMap)[1:]
    
    # Initialise the dictionary and read in patient as key and the tumour type as the value
    diseaseDict = {}
    for entry in diseaseCode:
        k = entry[0]
        # The column that specifies tumour or normal
        v = entry[97]
        diseaseDict[k] = v
    
    # Extract the header of the genomic file which is the patient
    header = rawTable[0]

    #Initialise a list to hold the phenotype labels
    phenotype = []
    for patient in header:
        if patient in diseaseDict.keys():
            phenotype.append(diseaseDict[patient])
    
    # Change the phenotype labels to be one word
    fixedPhenotype = []
    for case in phenotype:
        if case == 'Recurrent Tumor':
            case = 'Recurrent_Tumor'
        elif case == 'Primary Tumor':
            case = 'Primary_Tumor'
        elif case == 'Solid Tissue Normal':
            case = 'Normal'
        else:
            case = 'NA'
        fixedPhenotype.append(case)
           
    # Store the unique values of the phenoypes        
    sampleAnnotation = set(fixedPhenotype)
    
    # Number of samples
    sampleNo = len(phenotype)
    classNo = len(sampleAnnotation) 
    
    # Emit output
    print str(sampleNo) + '\t' + str(classNo) + '\t1'
    #print '#\t' + '\t'.join(sampleAnnotation)
    # The class labels need to be in order
    print '#\t' + '\tPrimary_Tumor\tNormal\tRecurrent_Tumor' 
    print '\t'.join(fixedPhenotype)
    
if __name__ == '__main__':
    main()