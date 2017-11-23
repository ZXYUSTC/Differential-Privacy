"""Collector in Smart Homes"""
__author__ = 'DWade'
import math
class Collector:

    p=0     #the estimated p
    q=0.5 #
    a=0
    b=0
    s=0
    e=0
    W=[] #the estimated array

    def __init__(self,p,q):
        self.p=p
        self.q=q
        self.a=(1-0.5*p)*(1-0.5*p)+p*q*(1-0.5*p)
        self.b=0.25*p*p+p*q*(1-0.5*p)
        for i in range(128):
            self.W.append(0)

    def receiver(self,bloombits,s,e):
        num=bloombits.count(1)
        if 1-2*self.q==0:
            self.p=0.5
            self.p=2*(num-1)/(e-s-1)
        else:
            self.p= (-2*((e-s+11)*self.q-1)+2*math.sqrt(((e-s+1)*self.q-1)-(1-num)*(1-2*self.q)))
        self.a = (1 - 0.5 * self.p) * (1 - 0.5 * self.p) + self.p * self.q * (1 - 0.5 * self.p)
        self.b = 0.25 * self.p * self.p + self.p * self.q * (1 - 0.5 * self.p)
        #self.a=0.75
        #self.b=0.25
        for i in range(s,e+1):
            if bloombits[i]==1:
                self.W[i]+=(1-self.b)/(self.a-self.b)
            else:
                self.W[i]+=self.b/(self.b-self.a)
    def getResult(self):
        return self.W

