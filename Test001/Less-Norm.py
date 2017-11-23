
import math
from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt

p=np.arange(1,0,-0.1)
q=0.5
e=[]
for d in p:
    e.append(math.log((d*d-4*d+4)/(d*d),math.e))
print(e)
N=100000
fo=open('data5.txt','a+')
mu=50
sigma=10
x=np.arange(0,101,1)
y=stats.norm.pdf(x,50,10)
z=np.zeros(101)
for i in np.arange(0,101):
    y[i]=y[i]*N
    y[i]=int(y[i])



for k in range(10):
    f=p[k]
    MyCollector = Collector(f, q)
    for index in range(101):
        for i in range(int(y[index])):
            data = BloomFilter(index, 4)
            bf = data.getBloomFilter()
            start = data.getSecurityDomain1()
            end = data.getSecurityDomain2()
            response = RRM(bf, f, q, start, end)
            pbf = response.randomer()
            MyCollector.receiver(pbf, start, end)
            # print(pbf)
    result = MyCollector.getResult()
    for j in range(0, 101):
        z[j] = int(result[j])
    a = 0
    b = 0
    for j in range(101):
        a += y[j]
        b += abs(z[j] - y[j])
    print(result)
    fo.write(str(b/a)+' ')
    MyCollector.setResult()
    del MyCollector
fo.write('\n')
fo.close()

