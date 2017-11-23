import math
from BloomFilter import *
from rrm import *
from Collector import *
import scipy.stats as stats
import numpy as np
import pylab as plt


p=np.arange(1,0,-0.1)
y=np.zeros(10)
z=np.zeros(10)
q=0.5
e=[]
for d in p:
    e.append(math.log((d*d-4*d+4)/(d*d),math.e))
fo=open('data-exp1.txt','r+')
test = fo.readline()
# print(test.split())
first = test.split()
i=0
for data in first:
    y[i]=data
    i+=1
plt.plot(e,y,color='g')
fo.close()
fo=open('data-exp2.txt','r+')
test = fo.readline()
# print(test.split())
first = test.split()
i=0
for data in first:
    z[i]=data
    i+=1
plt.plot(e,z,color='r')
plt.xlabel('exp('+r'$\epsilon$'+')',fontsize=20)
plt.ylabel(r'relative error',fontsize=20)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.title('Exponential Distribution',fontsize=20)

plt.show()
print(e),