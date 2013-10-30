#!/usr/bin/python

import csv, sys

file = open(sys.argv[1], 'U')
input = csv.reader(file, delimiter='\t')

data = []
for row in input:
    data.append(row)

for row in data:
        chromosome = row[0]
        chromosome = 'hs' + chromosome
        row[0] = chromosome
        print ' '.join(row)

#outputFile = sys.argv[2]
#writer = csv.writer(open(outputFile, 'w'), delimiter=" " )
#for row in input:
#    writer.writerow(row)