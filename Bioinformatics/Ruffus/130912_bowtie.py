#!/usr/bin/env python
"""

    ruffus_template.py  [--input_file]
                        [--log_file PATH]
                        [--verbose]
                        [--target_tasks]
                        [--jobs]
                        [--just_print]
                        [--flowchart]
                        [--key_legend_in_graph]
                        [--forced_tasks]

"""
import sys, os, re
import time

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   options


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888


if __name__ == '__main__':
    from optparse import OptionParser
    import StringIO

    parser = OptionParser(version="%prog 1.0", usage = "\n\n    %progs [options]")

    #
    #   general options: verbosity / logging
    #
    parser.add_option("-v", "--verbose", dest = "verbose",
                      action="count", default=1,
                      help="Print more verbose messages for each additional verbose level.")
    parser.add_option("-L", "--log_file", dest="log_file",
                      metavar="FILE",
                      type="string",
                      help="Name and path of log file")

    #
    #   pipeline options
    #
    parser.add_option("-i", "--input_file", dest="input_file",
                        action="append",
                        default = list(),
                        metavar="FILE",
                        type="string",
                        help="""The file(s) to use as input. If there are multiple 
                        files use the -i argument multiple times""")
    parser.add_option("-t", "--target_tasks", dest="target_tasks",
                        action="append",
                        default = list(),
                        metavar="JOBNAME",
                        type="string",
                        help="Target task(s) of pipeline.")
    parser.add_option("-j", "--jobs", dest="jobs",
                        default=1,
                        metavar="N",
                        type="int",
                        help="Allow N jobs (commands) to run simultaneously.")
    parser.add_option("-n", "--just_print", dest="just_print",
                        action="store_true", default=False,
                        help="Don't actually run any commands; just print the pipeline.")
    parser.add_option("--flowchart", dest="flowchart",
                        metavar="FILE",
                        type="string",
                        help="Don't actually run any commands; just print the pipeline "
                             "as a flowchart.")
    #
    #   Less common pipeline options
    #
    parser.add_option("--key_legend_in_graph", dest="key_legend_in_graph",
                        action="store_true", default=False,
                        help="Print out legend and key for dependency graph.")
    parser.add_option("--forced_tasks", dest="forced_tasks",
                        action="append",
                        default = list(),
                        metavar="JOBNAME",
                        type="string",
                        help="Pipeline task(s) which will be included even if they are up to date.")

    # get help string
    f =StringIO.StringIO()
    parser.print_help(f)
    helpstr = f.getvalue()
    (options, remaining_args) = parser.parse_args()


    #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    #                                             #
    #   Change this if necessary                  #
    #                                             #
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    #
    #   Add names of mandatory options,
    #       strings corresponding to the "dest" parameter
    #       in the options defined above
    #
    mandatory_options = [ ]

    #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    #                                             #
    #   Change this if necessary                  #
    #                                             #
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    def check_mandatory_options (options, mandatory_options, helpstr):
        """
        Check if specified mandatory options have b een defined
        """
        missing_options = []
        for o in mandatory_options:
            if not getattr(options, o):
                missing_options.append("--" + o)

        if not len(missing_options):
            return

        raise Exception("Missing mandatory parameter%s: %s.\n\n%s\n\n" %
                        ("s" if len(missing_options) > 1 else "",
                         ", ".join(missing_options),
                         helpstr))
    check_mandatory_options (options, mandatory_options, helpstr)


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   imports


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

from ruffus import *
import subprocess

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Functions

def run_cmd(cmd_str):
    """
    Throw exception if run command fails
    """
    process = subprocess.Popen(cmd_str, stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE, shell = True)
    stdout_str, stderr_str = process.communicate()
    if process.returncode != 0:
        raise Exception("Failed to run '%s'\n%s%sNon-zero exit status %s" %
                            (cmd_str, stdout_str, stderr_str, process.returncode))

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Logger

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

import logging
logger = logging.getLogger("run_parallel_blast")
#
# We are interesting in all messages
#
if options.verbose:
    logger.setLevel(logging.DEBUG)
    stderrhandler = logging.StreamHandler(sys.stderr)
    stderrhandler.setFormatter(logging.Formatter("    %(message)s"))
    stderrhandler.setLevel(logging.DEBUG)
    logger.addHandler(stderrhandler)

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888


#   Pipeline


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

###############################Put pipeline code here#####################################

#@transform(trimInput, suffix(".fastq"), [".trim.fastq", ".trimmSuccess.txt"]) #added touch file
#def trimmomatic(read1, outFiles):
#    read2 = re.sub('R1','R2', read1)
#    #split the output and touchFile
#    trimRead1, flagFile = outFiles
#    trimRead2 = re.sub('R1','R2', trimRead1)
#    unpair1 = read1 + 'unpair'
#    unpair2 = read2 + 'unpair'
#    headParams = 'java -Xmx4g -classpath ' 
#    classPath = '/Users/d.brown6/Bioinformatics/Trimmomatic-0.22/trimmomatic-0.22.jar '
#    trimOptions = 'org.usadellab.trimmomatic.TrimmomaticPE -threads 1 -phred33 -trimlog ' + read1 + '.trimLog.txt '
#    trailParams = ' ILLUMINACLIP:/Users/d.brown6/Bioinformatics/Trimmomatic-0.22/IlluminaAdaptersCustom.fa:2:40:15 LEADING:20 TRAILING:20 MINLEN:100'
# 
#    #------------------------------build shell command-------------------------------------  
#    commTrim = headParams + classPath + trimOptions + read1 + ' ' + read2 +\
#    ' ' + trimRead1 + ' ' + unpair1 + ' ' + trimRead2 + ' ' + unpair2 + ' ' + trailParams
#    #--------------------------------------------------------------------------------------
#    
#    started = time.strftime('%X %x %Z')
#    print 'running task trimmomatic at {0}'.format(started)
#    print commTrim
#    #run the command
#    #os.system(commTrim)
#
#    #touch file indicates success. It should be empty if there was success 
#    finished = time.strftime('%X %x %Z')
#    open(flagFile , 'w').write(finished)
#
#unzipInput = options.input_file
#
#@transform(unzipInput, suffix('.gz'), [r'../trimFastq/\1.fastq', 'unzipSuccess.txt'])
#def unzip(input1, outFiles):
#    input2 = re.sub('R1','R2', input1)
#    output, flagFile = outFiles
#    comm = 'gunzip ' + input1 + ' ' + input2
#    print comm
#    os.system(comm) 
#    #touch file indicates success. It should be have the completion time if there was success 
#    finished = time.strftime('%X %x %Z')
#    open(flagFile , 'w').write(finished)

os.chdir('/Users/d.brown6/Documents/RNAdata/danBatch1/trimFastq')
alignInput = options.input_file

#Hard code reference file locations for aligner. Change for Merri. human_g1k_v37.rev.1.bt2
refGenome = '/vlsci/VR0002/shared/Reference_Files/Indexed_Ref_Genomes/bowtie_Indexed/human_g1k_v37'

#@follows(unzip)
@transform(alignInput, suffix(".fastq"), [r'bowtie2Align/\1.bowtie.bam', ".alignSuccess.txt"])
def align(read1, outFiles):
    'Emit the aligned files in the bowtie2AlignDirectory. Used local mode with default settigs. Pipe output to samtools to produce a sorted bam file'
    read2 = re.sub('R1','R2', read1)
    rgID = read1[0:7]
    #split the output and touchFile
    output, flagFile = outFiles
    #------------------------------build shell command--------------------------------------
    alignNotes = "Local alignment (soft-clipping), report best alignment"
    headParams = 'bowtie2 --local -p 8 --rg-id ' + rgID
    midParams = ' -x ' + refGenome + ' -1 ' + read1 + ' -2 ' + read2
    tailParams = ' | samtools view -bS -o ' + output + ' -'
    comm = headParams + midParams + tailParams
    #---------------------------------------------------------------------------------------  
    started = time.strftime('%X %x %Z')
    print 'running task trimmomatic at {0}'.format(started)
    print comm
    #run the command
    #os.system(comm)
    #touch file indicates success. It should be have the completion time if there was success 
    finished = time.strftime('%X %x %Z')
    open(flagFile , 'w').write(finished)
    
#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Print list of tasks

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
if options.just_print:
    pipeline_printout(sys.stdout, options.target_tasks, verbose=options.verbose)


#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Print flowchart

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
elif options.flowchart:
    # use file extension for output format
    output_format = 'os.path.splitext(options.flowchart)[1][1:]'
    pipeline_printout_graph (open(options.flowchart, "w"),
                             output_format,
                             options.target_tasks,
                             no_key_legend = True)
#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

#   Run Pipeline

#88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
else:
    pipeline_run(options.target_tasks,  multiprocess = options.jobs,
                        logger = logger, verbose=options.verbose)