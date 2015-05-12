#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, csv, os

def readAfile(filenameString):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter=';')
    data = []
    for row in inputA:
        data.append(row)
    fileA.close()
    return data

def writeAfile(fileName, data2Bwritten):
    'Open a file and write rows in tab delimited format'
    w = open(fileName, 'w')        
    writer = csv.writer(w ,delimiter=",")
    for row in data2Bwritten:
        writer.writerow(row)
    w.close()
    
      
def main():
    parser = argparse.ArgumentParser(description="""
    Reads an input file that is output from the imageJ colocalisation plugin 'Squaash'. The data takes all the files put in a directory from
    different imaging fields and combines them into a usable form for analysis in R.
    """)
    parser.add_argument('-f', '--inputFolder', required=True, help='''The folder that contains the files from each field analysed by Squaash.''')
    #parser.add_argument('-i', '--inputData', required=True, help='''The file that is the raw data from one field analysed by Squaash.''')
    parser.add_argument('-s', '--slideName', required=False, help='The name of the slide used in the immunofluorescence. Will be used to add a filename to the row.')
    parser.add_argument('-o', '--outputData', required=False, help='The csv file you get at the end')
    args = parser.parse_args()
    
    # Parse commandline arguments
    slideName = args.slideName
    dir = os.getcwd()
    folder = os.listdir(args.inputFolder)
    columnHeader = dir + folder[0]
    print columnHeader
    
    # The container for the output file
#    outputFile = []
#    # Insert the column header from the first file in the directory
#    data = readAfile(file[0])
#    outputFile.append(data[0])
#    print folder
    
#    for file in folder:
#        print file
#        data = readAfile(file)
#        # Delete the second row which contains only parameters
#        del data[1]
    
    
#    data = readAfile(args.inputData)
#    # Remove the second row which contains only parameters
#    del data[1]
#    print data
#    
#    # Print the data to the standard output
#    for row in data:
#        print "\t".join(row)
       
# Boiler plate to run code
if __name__ == '__main__':
    main()