#!/usr/bin/env python

import subprocess, os

task = 'echox hello world > junk.txt'

#subprocess.check_output(task, stderr=subprocess.STDOUT, shell=True)
os.system(task)

nextTask = 'ls -lh > junk2.txt'

#subprocess.check_output(nextTask, stderr=subprocess.STDOUT, shell=True)
os.system(nextTask)