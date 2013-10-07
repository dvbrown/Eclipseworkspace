def htSeq(bamFile, outFiles):
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    headParams = '' 
    tailParams = ''
    midParams = ''
    comm = headParams + bamFile + ' OUTPUT=' + output + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    runJob(comm, 'htSeq', flagFile)