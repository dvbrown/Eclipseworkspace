import csv

# This is Daniel's set of useful functions he uses in other scripts.

def readAfile(filenameString, delimit='\t'):
    'Reads the input file into a dictionary object where the key is the first row'
    fileA = open(filenameString, 'U')
    inputA = csv.reader(fileA, delimiter=delimit)
    data = []
    for row in inputA:
        data.append(row)
    fileA.close()
    return data


def writeAfile(fileName, data2Bwritten):
    'Open a file and write rows in tab delimited format'
    w = open(fileName, 'w')
    writer = csv.writer(w ,delimiter="\t")
    for row in data2Bwritten:
        writer.writerow(row)
    w.close()


def fixVariables(inputFile, find, replace):
    'Read in a list of lists and if there is a match with find the replace it with replace!'
    result = []
    for entry in inputFile:
        # Make a list comprehension and store it as a variable
        findReplace = [replace if word==find else word for word in entry]
        result.append(findReplace)
    return result