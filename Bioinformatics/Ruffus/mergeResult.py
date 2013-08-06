NUMBER_OF_RANDOMS = 10000
CHUNK_SIZE = 1000


from ruffus import *
import time

import random, sys
import glob

#---------------------------------------------------------------
#
#   Create random numbers
#
@files(None, "random_numbers.list")
def create_random_numbers(input_file_name, output_file_name):
    f = open(output_file_name, "w")
    for i in range(NUMBER_OF_RANDOMS):
        f.write("%g\n" % (random.random() * 100.0))

#---------------------------------------------------------------
#
#   Split initial file
#
@follows(create_random_numbers)
@split("random_numbers.list", "*.chunks")
def step_5_split_numbers_into_chunks (input_file_name, output_files):
    """
        Splits random numbers file into XXX files of CHUNK_SIZE each
    """
    #
    #   clean up files from previous runs
    #
    for f in glob.glob("*.chunks"):
        os.unlink(f)
    #
    #
    #   create new file every CHUNK_SIZE lines and
    #       copy each line into current file
    #
    output_file = None
    cnt_files = 0
    for i, line in enumerate(open(input_file_name)):
        if i % CHUNK_SIZE == 0:
            cnt_files += 1
            output_file = open("%d.chunks" % cnt_files, "w")
        output_file.write(line)

#---------------------------------------------------------------
#
#   Calculate sum and sum of squares for each chunk file
#
@transform(step_5_split_numbers_into_chunks, suffix(".chunks"), ".sums")
def step_6_calculate_sum_of_squares (input_file_name, output_file_name):
    output = open(output_file_name,  "w")
    sum_squared, sum = [0.0, 0.0]
    cnt_values = 0
    for line in open(input_file_name):
        cnt_values += 1
        val = float(line.rstrip())
        sum_squared += val * val
        sum += val
    output.write("%s\n%s\n%d\n" % (repr(sum_squared), repr(sum), cnt_values))
    
def printHoorayAgain():
    print "Hooray times two"
    
def printWhoopeeAgain():
    print "Whoopee time!"

#-------------------------------------------------------------------
#Calculate the sum of squares for each chunk
@posttask(lambda: sys.stdout.write("hooray!\n"))
@posttask(printHoorayAgain, printWhoopeeAgain, touch_file("done"))
@merge(step_6_calculate_sum_of_squares, "variance.result")
def step_7_calculate_variance (input_file_names, output_file_name):
   "calculate variance the stupid way"
   output = open(output_file_name, "w")
   all_sum_squared = 0.0
   all_sum = 0.0
   all_cnt_values = 0.0
   
   #add up all the sum squared and sum and cnt values from all the chunks
   for input_file_name in input_file_names:
       sum_squared, sum, cnt_values = map(float, open(input_file_name).readlines())
       all_sum_squared += sum_squared
       all_sum += sum
       all_cnt_values += cnt_values
   all_mean = all_sum / all_cnt_values
   variance = (all_sum_squared - all_sum * all_mean)/(all_cnt_values)
   
   print >>output, variance

pipeline_run([step_7_calculate_variance, create_random_numbers], verbose = 5)