#!/usr/bin/python2.7

#This script will only work by running it multiple times, removing a duplicate entry each time.
#It compares two vectors with the same first entry and then keeps the higher sum entry
import csv, sys

f = csv.reader(open(sys.argv[1], 'U'),dialect='excel',delimiter='\t')
#read the file into a list of lists
bigList = []
for row in f:
    bigList.append(row)

#Initialise a list to output the end results
finalList = []

#initialise counter
def filterProbes():
    'This function does all the work but takes no arguments'
    x = 1
    while x <= len(bigList) -1:
    #if the first element of the next list is the same
        if bigList[x-1][0] == bigList[x][0]:
        #turn lists into floating point numbers. Remove the outer nesting of list
            firstList = bigList[x-1][1:]
            firstList = map(float, firstList)
            secondList = bigList[x][1:]
            secondList = map(float, secondList)
            #add one of the lists with the higher expression value
            newList = []
            if sum(firstList) > sum(secondList):
                newList.append(firstList)
            else:
                newList.append(secondList)    
        #put the gene name on the start of the list
            newList[0].insert(0, bigList[x-1][0])
            newList = newList[0]
            #append the new list to the output list
            finalList.append(newList)
            x = x + 1

#a container to store the gene names that have been duplicated
finalList = filterProbes()

compare =[]
for row in finalList:
    compare.append(row[0])

#go through the list that had duplicates removed and add the genes with a single entry
for row in bigList:
    if row[0] not in compare:
        finalList.append(row)
        #print finalList

outputFile = sys.argv[2]
writer = csv.writer(open(outputFile, 'w'), delimiter="\t" )
for row in finalList:
    writer.writerow(row)
#f.close()
#writer.close()    