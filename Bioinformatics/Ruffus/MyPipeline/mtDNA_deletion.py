import time, os, re, subprocess

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
    #subprocess.check_call(comm, stderr=subprocess.STDOUT ,shell=True)
    os.system(comm)
    #touch file indicates success. It should be empty if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)

def extractSecondaryAlignments(bamFile, outFiles):
    output, flagFile = outFiles
    os.system("samtools view -H {} > header.sam".format(bamFile))
    com = "samtools view -h {} | grep 'SA:' > {}".format(bamFile, output)
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
    