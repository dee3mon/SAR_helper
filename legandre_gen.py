# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:18:53 2020

@author: Dee
"""


def kron_jack_simbol(a, b):
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
            
def single_legandre_gen(N_length):
    import numpy as np
    a = np.zeros(N_length)
    a[0]=1
    for n in range(1, N_length):
        a[n] = kron_jack_simbol(n, N_length)
    return a
       

if __name__ == "__main__":
    N_length = 19
    test_seq=single_legandre_gen(N_length)
    print(test_seq)
    import numpy as np
    from numpy.fft import fft, ifft
    test_seq_spec = fft(test_seq)
    import matplotlib.pyplot as plt
    autocorrcirc = ifft(test_seq_spec * np.conj(test_seq_spec)).real
    plt.figure()
    plt.plot(autocorrcirc)
    autocorrlin = np.correlate(test_seq, test_seq, mode='full')
    plt.figure()
    plt.plot(autocorrlin)