__author__ = 'DWade'
import numpy as np
class BloomFilter:
    """
    Bloom Filter 128 bits
    """
    s=0
    e=0
    def __init__(self, data,len):
        self.bloombits=np.zeros(128,dtype=np.int16 )
        if data<=len:
            self.s=0
        else:
            self.s=data-len+1
        if (data+len-1)>=127:
            self.e=127
        else:
            self.e=data+len-1
        #for index in range(128):
            #self.bloombits.append(0)
        self.bloombits[data]=1

    def getBloomFilter(self):
        return self.bloombits
    def getSecurityDomain1(self):
        return self.s
    def getSecurityDomain2(self):
        return self.e


