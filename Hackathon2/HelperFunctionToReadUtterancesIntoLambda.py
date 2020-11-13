# -*- coding: utf-8 -*-
import random
import logging
import numpy as np
from nltk.util import ngrams
import os
import itertools



## Ensure that you create a folder with name 'intents' and put your utterances file there. 
## This has to further be put inside the folder containing your lambda_function.py
## so that you can zip it along with the other contents and upload to lambda.


path='./intents/'


def cleanLines(lines):
   for i in range(len(lines)):
       lines[i] = lines[i][:-1].split()
       for x in range(len(lines[i])):
           lines[i][x] = lines[i][x].lower()
   return lines


def readLines():
   for file in os.listdir(path):
     with open(path+file) as f:
       lines=f.readlines()
       lines=cleanLines(lines)
