import math as m
from scipy.stats import bernoulli as b
import numpy as np
import matplotlib.pyplot as plt


lam = 0.05
mu = 0.1
lpm = lam+mu
dt = 0.01
t_end = 50

def p0(t):
    return mu/lpm+lam/lpm*m.exp((-lpm)*t)


def p1(t):
    return lam/lpm-lam/lpm*m.exp((-lpm)*t)



def ana():
    l_p0 = []
    l_p1 = []
    for t in range(0,5001):
        if t == 0:
            continue
        l_p0.append(p0(t * 0.01))
        l_p1.append(p1(t * 0.01))
    x = np.arange(5000)/100
    plt.plot(x,l_p0,'-', label='p0',markersize=0.1,linewidth=1)
    plt.plot(x,l_p1,'-', label='p1',markersize=0.1,linewidth=1)
    plt.legend()
    plt.xlabel('t (minutes)')
    plt.ylim((0.0,1.0))
    plt.xlim((0,50))
    #print(f'p0={p0(t*0.01)}, p1={p1(t*0.01)}')


def sim():
    state = 0
    p0h_cnt = 0
    p1h_cnt = 0
    l_p0hat = []
    l_p1hat = []
    for t in range(0,5001):
        if t == 0:
            continue
        if state == 0:
            if b.rvs(lam) == 1:
                #print("change from 0 to 1")
                state = 1
            p0h_cnt += 1
        else:
            if b.rvs(mu) == 1:
                #print("change from 1 to 0")
                state = 0
            p1h_cnt += 1
        l_p0hat.append(p0h_cnt / (5000))
        l_p1hat.append(p1h_cnt / (5000))

    x = np.arange(5000) / 100
    plt.plot(x, l_p0hat, '-', label='p0hat', markersize=0.1, linewidth=1)
    plt.plot(x, l_p1hat, '-', label='p1hat', markersize=0.1, linewidth=1)
    plt.legend()
    #plt.xlabel('t (minutes)')
    #plt.ylim((0.0, 1.0))
    #plt.xlim((0, 50))
    #print(f'p0_hat={p0h_cnt/(10000)}, p1_hat={p1h_cnt/(10000)}')


if __name__ == '__main__':
    ana()
    sim()
    plt.show()