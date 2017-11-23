'''import numpy as np
from random import SystemRandom
a=np.zeros(5,dtype=np.int32)
for i in range(10):
    print(i)'''
import scipy.stats as stats
import numpy as np
import pylab as plt
'''
n=10
p=0.3
k=np.arange(0,21)
binomial =stats.binom.pmf(k,n,p)
print(binomial)
plt.plot(k,binomial,'-')
plt.title('Binomial:n=%i,p=%.2f' %(n,p),fontsize=15)
plt.xlabel('number of successes')
plt.ylabel('probability',fontsize=15)
plt.show()
'''
mu=50
sigma=10
x=np.arange(0,100,1)
y=stats.norm.pdf(x,50,10)
#plt.plot(x,y)
#plt.show()
for i in np.arange(0,100):
    y[i]=y[i]*100000
    y[i]=int(y[i])
   # print(y[i],'   ')
#plt.plot(x,y)
#plt.show()
#plt.hist(y)
#plt.show()


#plt.plot(x, y, color = 'r')
#plt.bar(x, y, alpha = .5, color = 'g')
plt.bar(x,y)

plt.show()
