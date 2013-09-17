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
    commTrim = headParams + classPath + trimOptions + read1 + ' ' + read2 +\
    ' ' + trimRead1 + ' ' + unpair1 + ' ' + trimRead2 + ' ' + unpair2 + ' ' + trailParams
    #--------------------------------------------------------------------------------------
    started = time.strftime('%X %x %Z')
    print 'running task trimmomatic at {0}'.format(started)
    print commTrim
    #run the command
    os.system(commTrim)
    #touch file indicates success. It should be empty if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)


def unzip(input1, outFiles):
    input2 = re.sub('R1','R2', input1)
    output, flagFile = outFiles
    comm = 'gunzip ' + input1 + ' ' + input2
    print comm
    os.system(comm) 
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)



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
    started = time.strftime('%X %x %Z')
    print 'running task bowtie at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)
    
    
    
def indexSamtools(bamFile, touchFile):
    #------------------------------build shell command--------------------------------------
    comm = 'samtools-gcc/0.1.18; samtools index ' + bamFile
    started = time.strftime('%X %x %Z')
    #---------------------------------------------------------------------------------------  
    print 'running task indexSamtools at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(touchFile , 'w').write(finished)


    
def markDuplicates(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = 'java -Xmx2g -jar /usr/local/picard/1.69/lib/MarkDuplicates.jar INPUT=' 
    tailParams = ' METRICS_FILE=duplicates.txt ASSUME_SORTED=true'
    comm = headParams + bamFile + ' OUTPUT=' + output + tailParams
    #---------------------------------------------------------------------------------------  
    started = time.strftime('%X %x %Z')
    print 'running task markDuplicates at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)



def reorderSam(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    params = 'java -Xmx2g -jar /usr/local/picard/1.69/lib/ReorderSam.jar INPUT='
    comm = params + bamFile + ' OUTPUT=' + output + ' REFERENCE' + refGenome
    #---------------------------------------------------------------------------------------  
    started = time.strftime('%X %x %Z')
    print 'running task reorderSam at {0}'.format(started)
    print comm
    #run the command
    os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)
    
    
    
def rnaSeQC(bamFile, outFiles):
    output, flagFile = outFiles
    sampleFile = bamFile[0:7] + '|' + 'Notes'
    #------------------------------build shell command--------------------------------------
    headParams = 'java -jar -mx1024m /vlsci/VR0002/shared/rnaseqc-1.1.7/RNA-SeQC_v1.1.7.jar -o '
    tailParams = output[0:7] + ' -r ' + refGenome + ' -rRNA ' + rRNA
    comm = headParams + tailParams + ' -s ' + sampleFile
    #---------------------------------------------------------------------------------------
    started = time.strftime('%X %x %Z')
    print 'running task rnaSeQC at {0}'.format(started)
    print comm
    #run the command
    #os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)