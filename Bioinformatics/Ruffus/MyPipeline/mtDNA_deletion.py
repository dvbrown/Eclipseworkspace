import time, os, re, subprocess, csv
import pandas as pd

# Global parameters
refTranscripts = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/genes.gtf'
picardLoc = '/Users/u0107775/Bioinformatics/picard-tools-2.0.1'

def runJob(comm, taskName, flagFile):
    '''An internal function used by the rest of the functions to spawn a process in the shell, capture the standard output 
    and generate a touch file. Runs the command in a shell and throws an exception when failure occurs'''
    started = time.strftime('%X %x %Z')
    print '\n################################################### RUNNNG TASK ' + taskName + ' at {0}'.format(started) + ' ###############################################'
    print comm + '\n'
    #run the command
    os.system(comm)
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)

def extractSecondaryAlignments(bamFile, outFiles):
    output, flagFile = outFiles
    os.system("samtools view -H {} > header.sam".format(bamFile))
    com = "samtools view {} | grep 'SA:' > {}".format(bamFile, output)
    runJob(com, "extractSecondaryAlignments", flagFile)

def addSamHeader(samFile, outFiles):
    output, flagFile = outFiles
    com = "cat header.sam {} | samtools view -bh > {}".format(samFile, output)
    runJob(com, "addSamHeader", flagFile)
    os.system("rm header.sam")

def sortSamtools(bamFile, outFiles):
    output, flagFile = outFiles
    com = "samtools sort {} > {}".format(bamFile, output)
    print com + "\n"
    runJob(com, "sortSamtools", flagFile)

def indexSamtools(bamFile, output):
    com = "samtools index {} > {}".format(bamFile, output)
    # No touch file therefore invoke os.system directly
    os.system(com)
    
#def convertToBed(bamfile, outFiles):
#    '''Convert the bam file of chimeric reads to bed and retain the secondary 
#    alignment flag as the score field in the bed file'''
#    output, flagFile = outFiles
#    # Write a temporary bed file
#    os.system('bedtools bamtobed -i {} > temp.bed'.format(bamfile))
#    # Extract the SA tag from same bam file and paste it as a column to the temp bed file
#    com = "samtools view -h {0} | awk {{'print $17'}} | paste temp.bed - > {1}".format(bamfile, output)
#    runJob(com, 'BamToBed SA', flagFile)
#    # Clean up bed file
#    os.system('rm temp.bed')
    
def convertToBed(bamfile, outFiles):
    '''Sort the bam file by coordinate to have split reads next to each other
    The convert to bed'''
    output, flagFile = outFiles
    com = "samtools sort -n {0} | bedtools bamtobed -i > {1}".format(bamfile, output)
    runJob(com, 'BamToBed SA', flagFile)
    
def collapseSplitReads(bedFile, outFiles):
    'Read in a bedfile as a pandas dataframe then output split reads side by side in a table'
    output, flagFile = outFiles
    # Read in data and split the first occurance of a read by its duplicate entries (alternate mappings)
    df = pd.read_csv(bedFile, sep="\t", header=None)
    dfLeft = df[df.duplicated(subset=3, keep='first')]
    dfRight = df[~df.duplicated(subset=3, keep='first')]
    # Merge by read name
    dfJoin = pd.merge(dfLeft, dfRight, how='inner', on=3)
    # Rename columns
    dfJoin.columns = ['chr_L', 'start_L', 'end_L', 'read_name', 'map_score_L', 'strand_L', 
    'chr_R', 'start_R', 'end_R', 'map_score_R', 'strand_R']
    # Set index of dataframe to read name, modifying the original object
    dfJoin.set_index('read_name', inplace=True)
    # Write to file
    dfJoin.to_csv(output, sep='\t')
    # Write the flagFile
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)
        
def filterSplitReads(bedFile, outFiles):
    'This script is work in progress - go up to '
    df = pd.read_csv("None-D99-1_S1_L001_bwa_RG_NA.sorted.SA.sort.split.bed", sep="\t", index_col = 0)

    # Filter reads that span the circular chromosome
    dfNo_origin = df[(df.start_L != 0) &  (df.start_R != 0)]
    
    # Filter split reads that align to separate strands
    dfStrand = dfNo_origin[dfNo_origin.strand_L == dfNo_origin.strand_R]
    
    dfStrand.to_csv('test.bed', sep='\t')
    # Next, only the deletions that are sequenced more than once for both sense and antisense strands 
    # and with identical breakpoints will be selected. The number of reads in both senses will be listed and summed.