import scipy.stats as stats
import numpy as np
import pylab as plt
import re


#lambd=0.05
d=0
x=np.arange(0,101,1)
z=np.zeros(101)
y=stats.norm.pdf(x,50,10)
for i in np.arange(0,101):
    y[i]=y[i]*100000
    y[i]=int(y[i])
    d+=y[i]
#z=np.zeros(100,int)
m=np.zeros(101,int)
n=np.zeros(101,int)

fo=open('data.txt','r+')
test=fo.readline()
#print(test.split())
first=test.split()
i=0
for data in first:
    z[i]=float(first[i])
    i=i+1
#print(z)

test=fo.readline()
second=test.split()
i=0
for data in second:
    m[i]=float(second[i])
    i=i+1
#print(m)

test=fo.readline()
third=test.split()
i=0
for data in third:
    n[i]=float(third[i])
    i=i+1
#print(n)
#y=stats.norm.pdf(x,50,10)
'''''''''
z the original pldp
m pldp
n rappor
'''

plt.plot(x,z,'b')
plt.plot(x,n,'r')
plt.plot(x,m,'g')
plot1=plt.plot(x,y,'k')
#plt.legend()
plt.xlabel(r'age',fontsize=20)
plt.ylabel(r'number',fontsize=20)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.title('Normal Distribution',fontsize=20)
plt.show()
#s1 = re.split('', test) #利用正则函数进行分割

'''
a=0
b=0
c=0

for i in range(100):
    a+=abs(y[i]-z[i])
    #print(a)
for i in range(100):
    c+=abs(y[i]-m[i])
for i in range(100):
    b+=abs(y[i]-n[i])
   # print(c)
#print(a)
#print(b)
print(d)

a=a/d
b=b/d
c=c/d
print(a)
print(b)
print(c)
'''