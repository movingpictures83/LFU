import random
import sys
from disk_struct import Disk
from page_replacement_algorithm import  page_replacement_algorithm
from CacheLinkedList import  CacheLinkedList
import numpy as np

import LFU_adaptive
import LFU_DECAY2
import LFU_gviet2
import LFU_LeCaR
import LFU

import PyIO
import PyPluMA

class LFUPlugin:
  def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

  def run(self):
        pass

  def output(self, outputfile):
    n = int(self.parameters["n"])
    infile = open(PyPluMA.prefix()+"/"+self.parameters["infile"], 'r')
    kind = self.parameters["kind"]
    outfile = open(outputfile, 'w')
    outfile.write("cache size "+str(n))
    if (kind == "LFU"):
       lfu = LFU.LFU(n)
    elif (kind == "LFU_adaptive"):
       lfu = LFU_adaptive.LFU_adaptive(n)
    elif (kind == "LFU_DECAY2"):
       lfu = LFU_DECAY2.LFU_DECAY2(n)
    elif (kind == "LFU_gviet2"):
       lfu = LFU_gviet2.LFU_gviet2(n)
    else:
       lfu = LFU_LeCaR.LFU_LeCaR(n)
    page_fault_count = 0
    page_count = 0
    for line in infile:
        line = line.strip()
        line = int(line)
        outfile.write("request: "+str(line))
        if lfu.request(line) :
            page_fault_count += 1
        page_count += 1

    
    outfile.write("page count = "+str(page_count))
    outfile.write("\n")
    outfile.write("page faults = "+str(page_fault_count))
    outfile.write("\n")
