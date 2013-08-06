#!/usr/bin/python2.7
#A function to transpose 384 well plate to a linear text file

import sys

fileName = sys.argv[1]
fileOpen = open(fileName, 'r')
print fileOpen

def TransposeTab(fileName):
    'A function to transpose a tab-delimited text file and transpose to a column vector' 
    result = []
    for line in fileName:
        line.strip(' ')
        line.split('\t')
        line.strip('\t')
        result.append(line +',')
    return result
  
transpose = TransposeTab(fileOpen)
transpose = str(transpose)
print transpose

#outputFile = open('output.txt', 'w')
#outputFile.write(transpose)

#outputFile.close()
#file.close()
