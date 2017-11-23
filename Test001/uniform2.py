
from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt



MyCollector=Collector(0.5,0.5)
#print(bf)
'''
mu=50
sigma=10
x=np.arange(0,101,1)
y=stats.norm.pdf(x,50,10)
'''
x=np.arange(10,30,0.2)
z=np.zeros(100)
y=np.zeros(100)
for i in np.arange(0,100):
    y[i]=1000

for index in range(100):
    for i in range(int(y[index])):
        data=BloomFilter(index,5)
        bf=data.getBloomFilter()
        start=data.getSecurityDomain1()
        end=data.getSecurityDomain2()
        response=RRM(bf,0.5,0.5,start,end)
        pbf=response.randomer()
        MyCollector.receiver(pbf,start,end)
    #print(pbf)
result=MyCollector.getResult()
#print(result)

for i in range(0,100):
    z[i]=int(result[i])

plt.bar(x,z,color='b')
#plt.plot(x,y)
plt.xlabel('age')
plt.ylabel('number')
plt.show()
fo=open('data3.txt','a+')
for i in range(100):
    fo.write(str(z[i])+' ')
fo.write('\n')
fo.close()





