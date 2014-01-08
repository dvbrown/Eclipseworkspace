#!/usr/bin/python

# This script will take a clinical report file and 2 gene expression files
# Gene expression file 1 = Agilent. File 2 = Affymetrix

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