"""Collector in Smart Homes"""
__author__ = 'DWade'
import math
class Collector:

    p=0     #the estimated p
    q=0 #
    a=0
    b=0

    W=[] #the estimated array
    Restult=[]
    def __init__(self,f,p,q):
        self.p=p
        self.q=q
        self.f=f
        self.a=0.5*f*(p+q)+(1-f)*q
        self.b=0.5*f*(p+q)+(1-f)*p
        #self.a=0.5
        #self.b=0.75
        for i in range(128):
            self.W.append(0)
            self.Restult.append(0)

    def receiver(self,bloombits):
        for i in range(0,128):
            if bloombits[i]==1:
                self.W[i]+=1
    def getResult(self):
        print(self.W)
        for i in range(0,128):
            self.Restult[i]=(self.W[i]-100000*self.b)/(self.a-self.b)
        r=[]
        for i in range(128):
            r.append(0)
        for i in range(128):
            r[i]=self.Restult[i]
        return r

