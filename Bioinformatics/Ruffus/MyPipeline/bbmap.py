# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:20:28 2016

@author: u0107775
"""

import time, os
import pandas as pd

# Global parameters
picardLoc = '/Users/u0107775/Bioinformatics/picard-tools-2.0.1/'
bioinformaticsDir = '/Users/u0107775/Bioinformatics/resources/rCRS_Mitochondira_fasta_noLines.fa'
referenceGenome = '/Users/u0107775/Bioinformatics/resources'
bbmap = "/Users/u0107775/Bioinformatics/bbmap/bbmap.sh"

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
    
def convertUnalignedBam(inputFile, outFiles):
    'The mark illumina adapters need a bam file'
    read1 = inputFile
    read2 = inputFile.replace('_R1_', '_R2_')
    output, flagFile = outFiles
    comm = """java -Xmx2G -jar {0}picard.jar FastqToSam \
    FASTQ={1} FASTQ2={2} \
    OUTPUT={3} \
    READ_GROUP_NAME=test \
    SAMPLE_NAME=test \
    LIBRARY_NAME=Illumina \
    PLATFORM_UNIT=H0164ALXX140820.2 \
    PLATFORM=illumina \
    SEQUENCING_CENTER=Brussels""".format(picardLoc, read1, read2, output)
    runJob(comm, "convertunaligned", flagFile)
    
def markAdapters(unalignmedBam, outFiles):
    output, flagFile = outFiles
    comm= """java -Xmx2G -jar {0}picard.jar MarkIlluminaAdapters \
    I={1} O={2} \
    M=markilluminaadapters_metrics.txt \
    TMP_DIR=/Users/u0107775/Bioinformatics/temp
    """.format(picardLoc, unalignmedBam, output)
    runJob(comm, "markAdapters", flagFile)
    
def alignMtDNA(inputFile, outFiles):
    'Align the sequencing reads using bbmap which apparently does deletions quite well'
    read1 = inputFile
    read2 = inputFile.replace('_R1_', '_R2_')
    output, flagFile = outFiles
    
    comm = "{4} in={0} in2={1} out={2} ref={3}/chrM.fa slow k=12 maxindel=16000".format(read1, read2, output, referenceGenome, bbmap)
    runJob(comm, "run bbmap", flagFile)