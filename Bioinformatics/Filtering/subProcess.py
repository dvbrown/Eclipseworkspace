#!/usr/bin/env python

import subprocess

task = 'echo hello world > junk.txt'

subprocess.check_output(task, stderr=subprocess.STDOUT, shell=True)

nextTask = 'ls -lh > junk2.txt'

subprocess.check_output(nextTask, stderr=subprocess.STDOUT, shell=True)