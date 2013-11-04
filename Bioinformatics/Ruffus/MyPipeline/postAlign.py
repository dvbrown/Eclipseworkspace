refTranscripts = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/genes.gtf'
rRnaBedFile = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/hg19_rRNA.bed'
countScript = "/vlsci/VR0238/dvbrown/dexseq_count.py"

from tasks import runJob
import re

def removeDuplicates(bamFile, outFiles):
    'Use the flag 0x400 to remove the duplicated reads'
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'samtools view -bh -F 0x400 ' + bamFile + ' > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'extractDuplicates', flagFile)

def extractDuplicates(bamFile, outFiles):
    'Use the flag 0x400 to get the duplicated reads'
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'samtools view -bh -f 0x400 ' + bamFile + ' > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'removeDuplicates', flagFile) 
    

def sortName(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'samtools sort -m 5000000000 -no ' + bamFile + ' - > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'sortReadName', flagFile)


def htSeq(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'samtools view -h ' + bamFile + ' | '
    midParams = 'python -m HTSeq.scripts.count  --stranded=no -m intersection-nonempty'
    tailParams = ' - ' + refTranscripts + ' > ' + output
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'htSeq', flagFile)
    
    
def dexSeqCount(bamFile, outFiles):
    '''Use the exon based gtf file from the previous step
    The -s option is required to use the unstranded option for the reference. Otherwise there is an error. 
    Input for DEXseq package in R.'''
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'samtools sort -m 5000000000 -no ' + bamFile + ' - | '
    midParams =  'samtools view -h - | '
    tailParams = 'python ' + countScript + ' -s no exonAnnotation.gtf ' + ' - ' + output
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------
    runJob(comm, 'contExons', flagFile)

def featureCounts(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'featureCounts -T 4 -b -p -a ' + refTranscripts + ' -t exon'
    tailParams = ' -S -g gene_id -o ' + output + ' ' + bamFile
    comm = headParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'featureCounts', flagFile)


def bamToBed(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'bamToBed -bedpe -i ' + bamFile + ' > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'makeBED', flagFile)
    

def interSectBED(bedFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'pairToBed -c -a ' + bedFile + ' -b ' + rRnaBedFile + ' > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'interSectBED', flagFile)
    
    
def defuse(read1, outFiles):
    '''Note that running deFuse again causes the program to continue where it left off
    You need to delete all the files in the output directory to make it completly restart. The annotate fusions subscript 
    crashes because the genome reference is given as the basebase in the config file (genome). I had to change this after 
    annotation crashed to (genome.fa). None of the R packages had the ada package. I had to install it in my home folder
    and create a R environmental variable echo 'R_LIBS_USER=~/R/x86_64-unknown-linux-gnu-library/2.15' >  $HOME/.Renviron
    '''
    read2 = re.sub('_R1_','_R2_', read1)
    output, flagFile = outFiles
    rgID = output[0:7]
    #------------------------------build shell command--------------------------------------
    headParams = '/usr/local/defuse/0.6.1-gcc/scripts/defuse.pl -c config.txt --1fastq '
    midParams = read1 + ' --2fastq ' + read2 + ' -o /vlsci/VR0238/shared/DanB_batch1/trimFastq/catFastq/'
    tailParams = rgID + '_out -p 8'
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'defuse', flagFile)
