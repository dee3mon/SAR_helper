# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:18:53 2020

@author: Dee
"""


def kron_jack_sinbol(a, b):
    from math import fmod, pow
    k = None
    if b==0:
        if abs(a)==1:
            k = 1
            return k
        elif abs(a)!=1:
            k = 0 
            return k
    if (fmod(a,2)==0 and fmod(b,2)==0):
        k = 0
        return k
    v = 0
    while fmod(b, 2)==0:
        v = v + 1
        b = b / 2
    if fmod(v, 2)==0:
        k = 1
    else:
        k = pow(-1, (pow(a,2) - 1)/8)
    if b<0:
        b = -b
        if a<0:
            k = -k
    while True:
        if a==0:
            if b>1:
                k = 0
                return k
            elif b==1:
                return k
        v = 0
        while fmod(a,2)==0:
            v = v + 1
            a = a / 2
        if fmod(v, 2)==1:
            k = k * pow(-1, (pow(b, 2) - 1)/8)
        k = k * pow(-1, (a-1)*(b-1)/4)
        r = abs(a)
        a = fmod(b, r)
        b = r
            
       
    
    


a1 = kron_jack_sinbol(1, 0)
a2 = kron_jack_sinbol(0, 0)
b1 = kron_jack_sinbol(4, 2)

for Niter in range(8):
    print (Niter, kron_jack_sinbol(Niter, 7))