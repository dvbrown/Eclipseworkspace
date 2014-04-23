#!/usr/bin/python2.7
#A script to parse 384 well files and transpose to column vector

import argparse, string, csv
import aUsefulFunctionsFiltering

def main():
    parser = argparse.ArgumentParser(description="""Reads an input file that is a linear representation of a 96 well plate and extracts the
    replicate level and binds them in columns""")
    parser.add_argument('-i', '--inputData', required=True, help='''The file that is the linear data from a 96 well experiment''')
    parser.add_argument('-r', '--replication', required=True, help='''The level of replication of the experiment ie 2 or 3 replicates. CURRENTLY WORKS FOR TRIPLICATE''')
    parser.add_argument('-f', '--fileType', required=True, help='''Whether this is a fluoro plate reader file (no headers)
        or a invasion assay data. Options = fluoro or invasion''')
    parser.add_argument('-o', '--outputData', required=False, help='The file you get at the end')
    args = parser.parse_args()
    
    # Input data. Take out the header if the data is an invasion assay
    data = aUsefulFunctionsFiltering.readAfile(args.inputData)
    if args.fileType == 'invasion':
        header = data[0]
        data = data[1:]
    elif args.fileType == 'fluoro':
        pass
    else:
        print 'This file type is not a valid invasion assay or data from a plate reader'
        
#    # Obtain in the well names
#    if args.fileType == 'invasion':
#        letters = list(string.ascii_lowercase)
#    elif args.fileType == 'fluoro':
#        letters = list(string.ascii_uppercase)
#    else:
#        print 'You have entered an invalid filetype'
#        
#    letters = letters[0:8]
#    number = range(1, 13)
#    # Paste the well letters and numbers
#    wells = []
#    for letter in letters:
#        for num in number:
#            x = letter + str(num)
#            wells.append(x)
    
    # Make a header
    header = ['well1', 'well2', 'well3' ,'rep1', 'rep2', 'rep3']
    print '\t'.join(header)
    
    
######################################## Build the list that will define replicates ################################################# 
    replicateLookup = [
                       ['a1','a2','a3'], ['a4','a5','a6'],['a7','a8','a9'],['a10','a11','a12'],
                       ['b1','b2','b3'], ['b4','b5','b6'],['b7','b8','b9'],['b10','b11','b12'],
                       ['c1','c2','c3'], ['c4','c5','c6'],['c7','c8','c9'],['c10','c11','c12'],
                       ['d1','d2','d3'], ['d4','d5','d6'],['d7','d8','d9'],['d10','d11','d12'],
                       ['e1','e2','e3'], ['e4','e5','e6'],['e7','e8','e9'],['e10','e11','e12'],
                       ['f1','f2','f3'], ['f4','f5','f6'],['f7','f8','f9'],['f10','f11','f12'],
                       ['g1','g2','g3'], ['g4','g5','g6'],['g7','g8','g9'],['g10','g11','g12'],
                       ['h1','h2','h3'], ['h4','h5','h6'],['h7','h8','h9'],['h10','h11','h12'],
                       ]
    

    
    if args.fileType == 'fluoro':
        replicateLookupN = []
        for group in replicateLookup:
            group = [string.upper(well[0]) for well in group]
            replicateLookupN.append(group)

#            for well in group:
#                lett = well[0]
#                num = well[1]
#                lettN = string.upper(lett)
#                well.replace(lett ,lettN + num)

                
                
    print replicateLookupN
     
######################################## This is the part of the script that does some work ################################################# 
    # If the data is in triplicate
    if args.replication == '3':
        for row in data:
            wellName = row[0]
            # Strip the file extension from the invasion well names
            if wellName.endswith('.tif'):
                wellName = wellName[:-4]
                
            # Search the well name of the data against the list of lists containing the replicate structure
            for group in replicateLookup:
                if wellName in group:
                    # Append to the replicate structure list
                    group.append(row[1])

############################################################################################################ 
    # Some error messages
    elif args.replication == '2':
        print "Duplicates ain't implemented yet"
        
    else:
        print "Invalid level of replication"
        
    # Write out to file if one is provided on command line
    if args.outputData == True:
        w = open(args.outputData, 'w')
        writer = csv.writer(w ,delimiter="\t")
        ###################################### Fix the iteration of this
        writer.writerow(zip(wells, plateMap2))
        ##################################
    


    for line in replicateLookup:
        print '\t'.join(line)

if __name__ == '__main__':
    main()        
