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
import sys, os
import tasks
import postAlign

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
logger = logging.getLogger(options.target_tasks)
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


#################################    PIPELINE CODE GOES HERE    #####################################

inputFile = options.input_file

#@transform(trimInput, suffix(".fastq"), [".trim.fastq", ".trimmSuccess.txt"]) #added touch file
#def trimReads(read1, outFiles):
#    tasks.tritrimmomatic(read1, outFiles)
#
#@transform(inputFile, suffix(".fastq"), [r'bowtie2Align/\1.bowtie.bam', ".alignSuccess.txt"])
#def align(inputFile, outFiles):
#    'Emit the aligned files in the bowtie2AlignDirectory. Used local mode with default settigs. Pipe output to samtools to produce a sorted bam file'
#    tasks.bowtie2(read1, outFiles)
#
#@transform(inputFile, suffix("_L001_R1_001.fastq.trim.bowtie.bam"), ['.trim.bowtie.merged.bam','mergeSuccess.txt'])
#def mergeAlignments(inputFile, outFiles):
#    'Take the 2 lanes and 2 parts per lane data and merge them together into a single bam file'
#    tasks.mergeBams(inputFile, outFiles)
#
#@transform(mergeAlignments, suffix(".bam"), ['.sortS.bam', ".sortSuccess.txt"])
#def sortSamtool(inputFile, outFiles):
#    'Sort the bam file by samtools, using the bowtie reference for markduplicates'
#    tasks.sortSamtools(inputFile[0], outFiles)
#
#@transform(sortSamtool, suffix(""), '.indexSucess.txt')
#def indexSamSort(inputFile, touchFile):
#    'Index the sorted bam file for use by mark duplicates'
#    tasks.indexSamtools(inputFile[0], touchFile)
#
#@follows(indexSamSort)
#@transform(sortSamtool, suffix(".bam"), ['.sortP.bam', ".sortPSuccess.txt"])
#def sortBamCoordinate(inputFile, outFiles):
#    'Sort the bam file by coordinate, using the bowtie reference for markduplicates \n'
#    tasks.reorderSam(inputFile[0], outFiles)
#     
#@transform(sortBamCoordinate, suffix(".bam"), ['.dedup.bam', ".deDupSuccess.txt"])
#def deDuplicate(inputFile, outFiles):
#    'Mark PCR duplicates, they are not removed'
#    tasks.markDuplicates(inputFile[0], outFiles)
#
#@transform(deDuplicate, suffix(".dedup.bam"), ['.rnaSeqc', ".alignQcSucess.txt"])
#def alignmentQC(inputFile, outFiles):
#    'Check alignments before proceeding with downstream analysis with RNAseQC'
#    tasks.rnaSeQC(inputFile[0], outFiles)
#
#@transform(inputFile, suffix(".dedup.bam"), [".getDup.bam",".getupSuccess.txt"])
#def extractPCRduplicates(inputFile, outFiles):
#    'Get the PCR duplicates to figure out if they are random or highly expressed genes'
#    postAlign.extractDuplicates(inputFile, outFiles)
#    
#@follows(extractPCRduplicates)
#@transform(inputFile, suffix(".dedup.bam"), [".rmDup.bam",".rmDupSuccess.txt"])
#def removePCRduplicates(inputFile, outFiles):
#    'Filter out the PCR duplicates'
#    postAlign.removeDuplicates(inputFile, outFiles)
#
#@transform(extractPCRduplicates, suffix(""), '.indexSucess.txt')
#def indexGetDup(inputFile, touchFile):
#    tasks.indexSamtools(inputFile[0], touchFile)
#    
#@transform(removePCRduplicates, suffix(""), '.indexSucess.txt')
#def indexRmDup(inputFile, touchFile):
#    tasks.indexSamtools(inputFile[0], touchFile)

@transform(inputFile, suffix(".bam"), [".sortName.bam", "sortNsucess.txt"])
def sortReadName(inputFile, outFiles):
    'sort the bam file by read name for use by HTSeq'
    postAlign.sortName(inputFile, outFiles)

@transform(sortReadName, suffix(".bam"), [".gem.txt", "htSeqSucess.txt"])
def countFeatures(inputFile, outFiles):
    'Use HTSeq with the intersection-nonempty mode.'
    postAlign.htSeq(inputFile[0], outFiles)
    
#@follows(countFeatures)
#@transform(inputFile, suffix("bam"), [".bed", "makeBEDSucess.txt"])
#def makeBED(inputFile, outFiles):
#    'Make a BED file for extra QCof alignments'
#    postAlign.bamToBed(inputFile, outFiles)
#    
#@transform(makeBED, suffix("bed"), [".rRNA.bed", "intersectSuccess.txt"])
#def intersectrRNA(inputFile, outFiles):
#    'Measure the degree of overlap between rRNA bed file and sample'
#    postAlign.interSectBED(inputFile, outFiles)

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
    output_format = os.path.splitext(options.flowchart)[1][1:]
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