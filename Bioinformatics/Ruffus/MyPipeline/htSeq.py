refTranscripts = '/vlsci/VR0002/shared/Reference_Files/human_UCSC_genes_v37_nochrprefix.gtf'
from tasks import runJob

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