import sys
from page_replacement_algorithm import  page_replacement_algorithm
from disk_struct import Disk
from priorityqueue import priorityqueue
# sys.path.append(os.path.abspath("/home/giuseppe/))

## Keep a LRU list.
## Page hits:
##      Every time we get a page hit, mark the page and also move it to the MRU position
## Page faults:
##      Evict an unmark page with the probability proportional to its position in the LRU list.
class LFU_DECAY2(page_replacement_algorithm):

    def __init__(self, N,decay=1):
        self.N = N
        self.PQ = priorityqueue(N)
        self.time = 0
        
    def get_N(self) :
        return self.N
    
    def request(self,page) :
        page_fault = False
        
        self.time += 1
        if self.time % self.N == 0 :
            self.PQ.decay(2)
        
        if page in self.PQ :
#         if self.PQ.contain(page) :
            page_fault = False
            self.PQ.increase(page)
        else :
            if self.PQ.size() == self.N:
                ## Remove LRU page
                self.PQ.popmin()
            self.PQ.add(page)
            page_fault = True
        
        return page_fault


    def get_data(self):
        return [list(self.freq)]

    def get_list_labels(self) :
        return ['L']


