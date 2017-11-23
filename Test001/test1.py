import numpy as np

import matplotlib.pyplot as plt

import matplotlib as mpl


# draw_line(labels,quants)
lambd=0.05
x=np.arange(0,101,1)
z=np.zeros(101,dtype=np.int16)
z[1]=1
z[2]=1
print(z.sum())
'''
y=lambd*np.exp(-lambd*x)
for i in np.arange(0,101):
    y[i]=y[i]*100000
    y[i]=int(y[i])
plt.bar(x,y,color='g')
plt.title('PLDP Mechanism with security domain')
plt.xlabel('residents\' age')
plt.ylabel('residents\'number')
plt.show()
'''