refTranscripts = '/vlsci/VR0002/shared/Reference_Files/human_UCSC_genes_v37_nochrprefix.gtf'
rRnaBedFile = 'someFile' #Find the rRNA bed file
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
    

def htSeq(bamFile, outFiles):
    output, flagFile = outFiles
    # The input needs to be sorted by readname. Pipe from samtools to HTSeq
    #------------------------------build shell command--------------------------------------
    headParams = 'samtools sort -no ' + bamFile + ' - | samtools view -h |'
    tailParams = 'python -m HTSeq.scripts.count  --stranded=yes -m intersection-nonempty'
    midParams = ' - ' + refTranscripts + ' > ' + output
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'htSeq', flagFile)
    
    
def makeBED(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'bamToBed -bedpe -i ' + bamFile + ' > ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'makeBED', flagFile)
    

def interSectBED(bedFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    comm = 'pairToBed [OPTIONS] -a ' + bedFile + ' -b ' + output
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'interSectBED', flagFile)