
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

lambd=0.05
x=np.arange(0,101,1)
z=np.zeros(101)
y=lambd*np.exp(-lambd*x)
for i in np.arange(0,101):
    y[i]=y[i]*100000
    y[i]=int(y[i])
plt.plot(x,y)
plt.show()
for index in range(101):
    for i in range(int(y[index])):
        data=BloomFilter(index,5)
        bf=data.getBloomFilter()
        response=RRM(bf,f,p,q)
        pbf=response.randomer()
        MyCollector.receiver(pbf)
    #print(pbf)
result=MyCollector.getResult()
#print(result)

for i in range(0,101):
    z[i]=int(result[i])

plt.bar(x,z,color='g')
plt.title('RAPPOR Mechanism')
plt.xlabel('age')
plt.ylabel('number')
plt.show()

fo=open('data1.txt','a+')
for i in range(101):
    fo.write(str(z[i])+' ')
fo.write('\n')
fo.close()






