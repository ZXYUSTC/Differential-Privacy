from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt

p=1/6
q=5/6
f=0.25

MyCollector=Collector(f,p,q)
#print(bf)

x=np.arange(10,30,0.2)
y=np.zeros(100)
for i in range(100):
    y[i]=1000
z=np.zeros(100)
for index in range(100):
    for i in range(1000):
        data=BloomFilter(index,5)
        bf=data.getBloomFilter()
        response=RRM(bf,f,p,q)
        pbf=response.randomer()
        MyCollector.receiver(pbf)
    #print(pbf)
result=MyCollector.getResult()
#print(result)

for i in range(0,100):
    z[i]=int(result[i])
plt.bar(x,z,color='g')
plt.title('RAPPOR Mechanism')
plt.xlabel('age')
plt.ylabel('number')
plt.show()

fo=open('data3.txt','a+')
for i in range(100):
    fo.write(str(z[i])+' ')
fo.write('\n')
fo.close()






