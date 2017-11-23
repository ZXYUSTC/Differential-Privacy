import numpy as np
import pylab as plt
import scipy.stats as stats
import math

d = 0
x = np.arange(0, 100, 1)
y = np.arange(0, 100, 1)
#y = stats.norm.pdf(x, 50, 10)
for i in range(100):
    y[i] = 1000
    d += y[i]
z = np.zeros(100, int)
m = np.zeros(100, int)
n = np.zeros(100, int)

fo = open('data2.txt', 'r+')
test = fo.readline()
# print(test.split())
first = test.split()
i = 0
for data in first:
    z[i] = float(first[i])
    i = i + 1
# print(z)

test = fo.readline()
second = test.split()
i = 0
for data in second:
    m[i] = float(second[i])
    i = i + 1
# print(m)

test = fo.readline()
third = test.split()
i = 0
for data in third:
    n[i] = float(third[i])
    i = i + 1
# print(n)
# y=stats.norm.pdf(x,50,10)
'''
plt.bar(x, m, color='g')
plt.title('RAPPOR Mechanism')
plt.xlabel('age')
plt.ylabel('number')
plt.show()
'''
'''
plt.plot(x,z,'b')
plt.plot(x,m,'g')
plt.plot(x,n,'r')
plot1=plt.plot(x,y,'k')
#plt.legend(plot1,'norm distribution')
plt.show()
'''
'''
# s1 = re.split('', test) #利用正则函数进行分割
'''
a=0
b=0
c=0
n1=0.0
n2=0
n3=0
n4=0.00
for i in range(100):
    n1+=y[i]
for i in range(100):
    if n[i]<=0:
        n[i]=2*abs(n[i])
    n4+=n[i]
for i in range(100):
    if m[i]<=0:
        m[i]=2*abs(m[i])
    n3+=m[i]
print(n1)
print(n4)
print(n3)
p=[]
q=[]
a=[]
for i in range(100):
    p.append(n[i]/n4)
for i in range(100):
    q.append(y[i]/n1)
for i in range(100):
    a.append(m[i]/n3)
print(p)
print(q)
print(m)
for i in range(100):
    if p[i]!=0 and q[i]!=0:
        c+=p[i]*math.log(p[i]/q[i],math.e)
print(c)
for i in range(100):
    if a[i]!=0 and q[i]!=0:
        b+=a[i]*math.log(a[i]/q[i],math.e)
print(b)
'''
for i in range(101):
    a+=abs(y[i]-z[i])
    #print(a)
for i in range(101):
    b+=abs(y[i]-m[i])
for i in range(101):
    c+=abs(y[i]-n[i])
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
