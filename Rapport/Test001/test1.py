from BloomFilter import *
from rrm import *
from Collector import *
f=0
p=0.5
q=0.75
data=BloomFilter(5,5)
bf=data.getBloomFilter()
response=RRM(bf,f,p,q)
pbf=response.randomer()
print(pbf)
num=pbf.count(1)
print(num)