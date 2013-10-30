import time, os, re, subprocess

# Global parameters
refGenome = '/vlsci/VR0002/shared/Reference_Files/Indexed_Ref_Genomes/bowtie_Indexed/human_g1k_v37'
refGenomeSort = '/vlsci/VR0002/shared/Reference_Files/Indexed_Ref_Genomes/bowtie_Indexed/human_g1k_v37.fasta'
rRNA = './hg19_ribosome_gene_locations.list'
refTranscripts = '/vlsci/VR0238/shared/DanB_batch1/trimFastq/bowtie2Align/mergeMarkDupBam/genes.gtf'

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


def trimmomatic(read1, outFiles):
    read2 = re.sub('R1','R2', read1)
    #split the output and touchFile
    trimRead1, flagFile = outFiles
    trimRead2 = re.sub('R1','R2', trimRead1)
    unpair1 = read1 + 'unpair'
    unpair2 = read2 + 'unpair'
    headParams = 'java -Xmx4g -classpath ' 
    classPath = '/Users/d.brown6/Bioinformatics/Trimmomatic-0.22/trimmomatic-0.22.jar '
    trimOptions = 'org.usadellab.trimmomatic.TrimmomaticPE -threads 1 -phred33 -trimlog ' + read1 + '.trimLog.txt '
    trailParams = ' ILLUMINACLIP:/Users/d.brown6/Bioinformatics/Trimmomatic-0.22/IlluminaAdaptersCustom.fa:2:40:15 LEADING:20 TRAILING:20 MINLEN:100'
    #------------------------------build shell command-------------------------------------  
    comm = headParams + classPath + trimOptions + read1 + ' ' + read2 +\
    ' ' + trimRead1 + ' ' + unpair1 + ' ' + trimRead2 + ' ' + unpair2 + ' ' + trailParams
    #--------------------------------------------------------------------------------------
    runJob(comm, 'trimReads', flagFile)

def fastqc(read, outFiles):
    'A stub for use in complete pipeline. Not functional yet'
    read2 = re.sub('R1','R2', read1)
    #split the output and touchFile
    output, flagFile = outFiles
    comm = 'Insert Fastqc command here'
    runJob(comm, 'fastQC', flagFile)

def unzip(input1, outFiles):
    input2 = re.sub('R1','R2', input1)
    output, flagFile = outFiles
    comm = 'gunzip ' + input1 + ' ' + input2
    print comm
    subprocess.check_output(comm, stderr=subprocess.STDOUT, shell=True) 
    #touch file indicates success. It should be have the completion time if there was success 
    runJob(comm, 'unzip', flagFile)
 
def concatenateFastq(read1, outFiles):
    "Put the fastq files together. Remove the newline between files using grep. "
    output, flagFile = outFiles
    output2 = re.sub('R1','R2', output)
    read1a = re.sub('_001.','_002.', read1)
    read1b = re.sub('_L001_','_L002_', read1)
    read1c = re.sub('_001.','_002.', read1b)
    read2 = re.sub('_R1_','_R2_', read1)
    read2a = re.sub('_001.','_002.', read2)
    read2b = re.sub('_L001_','_L002_', read2)
    read2c = re.sub('_001.','_002.', read2b)
    #------------------------------build shell command--------------------------------------
    read1Params =  'cat ' + read1 + ' ' + read1a + ' ' + read1b + ' ' + read1c + ' | '
    read2Params = 'cat ' + read2 + ' ' + read2a + ' ' + read2b + ' ' + read2c + ' | ' 
    tailParams = 'grep -v ^\$  > '
    commRead1 = read1Params + tailParams + output
    commRead2 = read2Params + tailParams + output2
    #--------------------------------------------------------------------------------------- 
    runJob(commRead1, 'concatenateFastq', flagFile)
    runJob(commRead2, 'concatenateFastq', flagFile)

def bowtie2(read1, outFiles):
    read2 = re.sub('R1','R2', read1)
    rgID = read1[0:7]
    #split the output and touchFile
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'bowtie2 --local -p 8 --rg-id ' + rgID
    midParams = ' -x ' + refGenome + ' -1 ' + read1 + ' -2 ' + read2
    tailParams = ' | samtools view -bS -o ' + output + ' -'
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'bowtie2', flagFile)


def alignTopHat(read1, outFiles):
    """Alignment is able to be split over many cores, Merri has 8 cores per node. 
    As the library had mean size of 270bp set mate inner distance to 70.
    Use a gene model annotations -G and reuse this annotation index file by storing it in a directory.
    This step should be done where the bpipe config file is configured for the smpt queue.""" 
    read2 = re.sub('_R1_','_R2_', read1)
    rgID = read1[0:7]
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'tophat -p 8 -G ' + refTranscripts + ' --transcriptome-index=transcriptome_data/known'
    juncParams = ' --read-mismatches 4 --read-gap-length 4 --max-multihits  1 --mate-inner-dist  1'
    midParams = ' --read-edit-dist 4 -o ' + rgID +'_out '
    tailParams = refGenome + ' ' + read1 + ' ' + read2
    comm = headParams + juncParams + midParams + tailParams
    #---------------------------------------------------------------------------------------
    runJob(comm, 'TopHat', flagFile)


def mergeBams(bamFile, outFiles):
    output, flagFile = outFiles
    sample2 = re.sub('_L001_','_L002_', bamFile)
    sample3 = re.sub('_001.','_002.', bamFile)
    sample4 = re.sub('_001.','_002.', sample2)
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx10g -jar /usr/local/picard/1.96/lib/MergeSamFiles.jar'
    midParams = ' INPUT=' + bamFile + ' INPUT=' + sample2 + ' INPUT=' + sample3 + ' INPUT=' + sample4
    tailParams = ' CREATE_INDEX=true MAX_RECORDS_IN_RAM=750000 TMP_DIR=/vlsci/VR0238/shared/tmp'
    comm = headParams + midParams + ' OUTPUT=' + output + tailParams
    #---------------------------------------------------------------------------------------
    runJob(comm, 'mergeBam', flagFile)


def sortSam(bamFile, outFiles):
    output, flagFile = outFiles
    comm = 'java -Xmx4g -jar /usr/local/picard/1.96/lib/SortSam.jar INPUT=' + bamFile + ' OUTPUT=' + output + ' SORT_ORDER=coordinate MAX_RECORDS_IN_RAM=1000000'
    started = time.strftime('%X %x %Z')
    print 'running task reorderSam at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)
      
    
def indexSamtools(bamFile, touchFile):
    #------------------------------build shell command--------------------------------------
    comm = 'samtools index ' + bamFile
    started = time.strftime('%X %x %Z')
    #---------------------------------------------------------------------------------------  
    print 'running task indexSamtools at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(touchFile , 'w').write(finished)


def addOrReplaceReadGroups(bamFile, outFiles):
    output, flagFile = outFiles
    RGID = bamFile[0:26]
    RGSM = bamFile[0:7]
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx2g -jar /usr/local/picard/1.96/lib/AddOrReplaceReadGroups.jar VALIDATION_STRINGENCY=LENIENT INPUT='
    tailParams = ' SORT_ORDER=coordinate ' + 'RGID=' + RGID + ' RGLB=RNA RGPL=ILLUMINA RGPU=H14NTADXX RGSM='
    comm = headParams + bamFile + ' ' + 'OUTPUT=' + output + ' ' + tailParams + RGSM
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'changeReadGroups', flagFile)
    
    
def markDuplicates(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx4g -jar /usr/local/picard/1.96/lib/MarkDuplicates.jar INPUT=' 
    tailParams = ' CREATE_INDEX=true MAX_RECORDS_IN_RAM=750000 TMP_DIR=/vlsci/VR0238/shared/tmp'
    midParams = ' METRICS_FILE=duplicates.txt ASSUME_SORTED=true'
    comm = headParams + bamFile + ' OUTPUT=' + output + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'markDuplicates', flagFile)



def reorderSam(bamFile, outFiles):
    output, flagFile = outFiles
    #had to create a temporary directory in my account as the default one is likely full
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx4g -jar /usr/local/picard/1.96/lib/ReorderSam.jar '
    midParams = 'CREATE_INDEX=true MAX_RECORDS_IN_RAM=750000 TMP_DIR=/vlsci/VR0238/shared/tmp '
    tailParams = 'INPUT=' + bamFile + ' OUTPUT=' + output + ' REFERENCE=' + refGenomeSort
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'reorderSam', flagFile)
    
    
def sortSamtools(bamFile, outFiles):
    output, flagFile = outFiles
    comm = 'samtools sort -o -m 8000000000 ' + bamFile + ' - > ' + output
    runJob(comm, 'sortSamtools', flagFile)

    
def rnaSeQC(bamFile, outFiles):
    output, flagFile = outFiles
    sampleFile = repr(bamFile[0:7] + '|' + bamFile + '|' + 'Notes')
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx4g -jar /vlsci/VR0002/shared/rnaseqc-1.1.7/RNA-SeQC_v1.1.7.jar -o ./'
    tailParams = output[0:7] + ' -r ' + refGenomeSort + ' -rRNA ' + rRNA + ' -t ' + refTranscripts
    comm = headParams + tailParams + ' -s ' + sampleFile
    #---------------------------------------------------------------------------------------
    runJob(comm, 'rnaSeQC', flagFile)