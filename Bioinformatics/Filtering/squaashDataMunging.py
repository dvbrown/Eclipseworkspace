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
    different imaging fields and combines them into a usable form for analysis in R. The script must be run in from the directory with the raw data.
    Usage: squaashDataMunging -s 'Name'
    """)
    parser.add_argument('-s', '--slideName', required=True, help='The name of the slide used in the immunofluorescence. Will be used to add a filename to the row.')
    parser.add_argument('-o', '--outputData', required=False, help='The csv file you get at the end. Otherwise redirect output')
    args = parser.parse_args()
    
    # Parse commandline argument
    slideName = args.slideName
    fold = os.listdir(".")
    # Retain only files from Squaash via list comprehension
    folder = [s for s in fold if "merged" in s]
    
    # The container for the output file
    outputFile = []
    # Insert the column header from the first file in the directory
    data = readAfile(folder[0])
    outputFile.append(data[0])
    
    # Extract the data from each file
    for f in folder:
        data = readAfile(f)
        # Retain only the last (3rd) row which contains the measurements
        row = data.pop(2)
        # Add the image name to the first element of the row
        row[0] = slideName + "_" + row[0]
        outputFile.append(row)
    
    # Print the data to the standard output
    for row in outputFile:
        print ",".join(row)
       
# Boiler plate to run code
if __name__ == '__main__':
    main()