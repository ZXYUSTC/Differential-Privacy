"""Randomized Response Mechanism"""
__author__ = 'DWade'

from random import SystemRandom
"""

"""

class RRM:

    eplison = 0  #the privacy budget
    p=0        #the first probability
    q=0        #the second probability
    s=0         #the start of security domain
    e=0         #the end of security domain

    def __init__(self,bloombits,p,q,s,e):
        self.eplison=0
        self.p=p
        self.q=q
        self.bloombits=bloombits
        self.b1=[]
        self.b2=[]
        self.result=[]
        self.s=0
        self.e=127
        for i in range(128):
            self.b1.append(0)
            self.b2.append(0)
            self.result.append(0)

    def randomer(self):
        for i in range(128):
            if i>=self.s and i<=self.e:
                rand = SystemRandom()
                probability = rand.random()
                if self.bloombits[i]==1:
                    bit = probability < 1-0.5*self.p
                    if bit==1:
                        self.b1[i]=1
                    else:
                        self.b1[i]=0
                else:
                    bit = probability<0.5*self.p
                    if bit==1:
                        self.b1[i]=1
                    else:
                        self.b1[i]=0
        for i in range(128):
            if i >= self.s and i <= self.e:
                rand = SystemRandom()
                probability=rand.random()
                if self.bloombits[i]==1:
                    bit = probability < 1-0.5*self.p
                    if bit==1:
                        self.b2[i]=1
                    else:
                        self.b2[i]=0
                else:
                    bit = probability<0.5*self.p
                    if bit==1:
                        self.b2[i]=1
                    else:
                        self.b2[i]=0

        for i in range(128):
            rand=SystemRandom()
            probability=rand.random()
            if self.b1[i]==1 and self.b2[i]==1:
                self.result[i]=1
            if self.b1[i]==0 and self.b2[i]==0:
                self.result[i]=0
            if self.b1[i]==1 and self.b2[i]==0:
                bit=probability<self.q
                if bit==1:
                    self.result[i]=1
                else:
                    self.result[i]=0
            if self.b1[i]==0 and self.b2[i]==1:
                bit=probability<self.q
                if bit==1:
                    self.result[i]=1
                else:
                    self.result[i]=0
        return self.result
    def getSecurityDomain1(self):
        return self.s
    def getSecurityDomain2(self):
        return self.e



