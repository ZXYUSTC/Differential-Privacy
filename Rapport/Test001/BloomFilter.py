__author__ = 'DWade'

class BloomFilter:
    """
    Bloom Filter 256 bits
    2 hash functions
    """
    bloomfits=[]
  #  for index in range(256):

    def __init__(self, data,len):
        self.bloombits=[]
        for index in range(128):
            self.bloombits.append(0)
        self.bloombits[data]=1
       # self.bloombits[data+128]=1

    def getBloomFilter(self):
        return self.bloombits


