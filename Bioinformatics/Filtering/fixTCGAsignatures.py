#!/usr/bin/python2.7

import os, csv

os.chdir('/Users/d.brown6/Documents/public-datasets/TCGA/classficationSignature/')
inFile = '131022_tryReformatThis.txt'
outFile = 'output.txt'

data = []
f = open(inFile, 'U')
files = csv.reader(f, delimiter='\t')
for row in files:
    data.append(row)
    
dataHeader = data[0]
data = data[1:]    
    
print dataHeader
    
for line in data:
    nums = line[3:7]
    mode = line[7]
    for position, item in enumerate(nums):
        if item != mode:
            line.append(position)
 
 
#for line in data:
#    ty = line[8]
#    subtype = line[3]       
#    if ty == 0:
#            subtype.replace(0, 'Proneural')
#    elif ty == 1:
#        subtype = 'Neural'
#    elif ty == 2:
#        subtype = 'Classical'
#    else:
#        subtype = 'Mesenchymal'
#        #print '\t'.join(line[1:7])
#    print line

w = open(outFile, 'w')        
writer = csv.writer(w ,delimiter="\t")
for row in data:
    writer.writerow(row)

f.close()
w.close() 