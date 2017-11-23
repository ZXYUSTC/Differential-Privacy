from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt


N=100000
fo=open('data5.txt','a+')
#print(bf)
mu=50
sigma=10
x=np.arange(0,101,1)
y=stats.norm.pdf(x,50,10)
z=np.zeros(101)
for i in np.arange(0,101):
    y[i]=y[i]*N
    y[i]=int(y[i])

p=1
q=0.5
MyCollector=Collector(p,q)
for index in range(101):
    for i in range(int(y[index])):
        data=BloomFilter(index,4)
        bf=data.getBloomFilter()
        start=data.getSecurityDomain1()
        end=data.getSecurityDomain2()
        response=RRM(bf,p,q,start,end)
        pbf=response.randomer()
        MyCollector.receiver(pbf,start,end)
    #print(pbf)
result=MyCollector.getResult()
#print(result)

for i in range(0,101):
    z[i]=int(result[i])

plt.bar(x,z,color='g')
plt.title('PLDP Mechanism with security domain')
plt.xlabel('residents\' age')
plt.ylabel('residents\'number')
plt.show()

a=0
b=0
for i in range(101):
    a+=y[i]
    b+=abs(z[i]-y[i])
print(b/a)













