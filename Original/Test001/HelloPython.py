from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt



MyCollector=Collector(0.5,0.5)
#print(bf)
mu=50
sigma=10
x=np.arange(0,101,1)
y=stats.norm.pdf(x,50,10)
z=np.zeros(101)
for i in np.arange(0,101):
    y[i]=y[i]*100000
    y[i]=int(y[i])

for index in range(101):
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

for i in range(0,101):
    z[i]=int(result[i])
plt.bar(x,z,color='g')
plt.title('PLDP Mechanism without security domain')
plt.xlabel('residents\' age')
plt.ylabel('residents\' number')
plt.show()
fo=open('data.txt','a+')
for i in range(101):
    fo.write(str(z[i])+' ')
fo.write('\n')
fo.close()


