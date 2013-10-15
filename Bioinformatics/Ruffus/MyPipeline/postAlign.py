refTranscripts = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/ensGene.gtf'
rRnaBedFile = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/hg19_rRNA.bed'

from tasks import runJob

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
    midParams = 'python -m HTSeq.scripts.count  --stranded=reverse -m intersection-nonempty'
    tailParams = ' - ' + refTranscripts + ' > ' + output
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'htSeq', flagFile)
    
    
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