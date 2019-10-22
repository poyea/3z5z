import numpy.random as rnd
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

import threading

n = 10000
m = 100000
k = 101
chi = 124.342


lstD = []
def bigD():
    def calcD(lst, n, k):
        expected = n/k
        summ = 0
        for i in range(0,k):
            summ += (lst[i] - expected)**2
        return summ*k/n

    lst = [0 for _ in range(0,k)]
    for _ in range(0,n):
        num = rnd.uniform(0,1)
        pos = math.floor(num*k)
        lst[pos] += 1
    val = calcD(lst, n, k)
    lstD.append(val)
    return val


def run():
    for _ in range(0,m+1):
        t = threading.Thread(target=bigD)
        t.daemon = True
        t.start()
        #lstD.append(bigD())
    print(len(lstD))
    t = np.arange(0, 160 , 0.1)
    plt.hist(lstD, bins=k)
    plt.plot(t,11000*stats.chi2.pdf(t, df=k-1))
    plt.axvline(x=chi, color='r')
    plt.show()