# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:48:13 2020

@author: PranavM
"""
#MODULE OS
import os
import time
curDir= os.getcwd()

print(curDir)

os.mkdir('newDir')
os.rename('newDir','nreDir2')

time.sleep(2)

help(os)

#MODULE SYS

import sys
sys.stderr.write('This is stderr test\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text')

print(sys.argv)
