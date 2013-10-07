#!/usr/bin/env python

import subprocess as sp

task = 'echo hello world > junk.txt'

print 'Please print this to the standard out'
sp.check_call(task,  shell=True)
#os.system(task)

comm = 'ls'
nextTask = ' -2'# > junk2.txt
run = comm + nextTask

value = sp.check_output(run, shell=True, stderr=sp.STDOUT)


#os.system(nextTask)