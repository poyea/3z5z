import math as m
from scipy.stats import expon as e
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
    for t in range(0,10001):
        if t == 0:
            continue
        l_p0.append(p0(t * 0.01))
        l_p1.append(p1(t * 0.01))
    x = np.arange(10000) / 100
    plt.plot(x, l_p0, '-', label='p0', markersize=0.1, linewidth=1)
    plt.plot(x, l_p1, '-', label='p1', markersize=0.1, linewidth=1)
    plt.legend()
    plt.xlabel('t (minutes)')
    plt.ylim((0.0, 1.0))
    plt.xlim((0, 50))
    #print(f'p0={p0(t*0.01)}, p1={p1(t*0.01)}')


def sim():
    state = 0
    p0h_cnt = 0
    p1h_cnt = 0
    l_p0hat = []
    l_p1hat = []
    t = 0
    while t < 10001:
        if state == 0:
            state = 1
            ran = int(round(e.rvs(1/lam)))
            t += ran
            p0h_cnt += ran
            l_p0hat.extend([p0h_cnt/10000 for _ in range(0,ran)])
            l_p1hat.extend([p1h_cnt / 10000 for _ in range(0, ran)])
        else:
            state = 0
            ran = int(round(e.rvs(1/mu)))
            t += ran
            p1h_cnt += ran
            l_p0hat.extend([p0h_cnt/10000 for _ in range(0,ran)])
            l_p1hat.extend([p1h_cnt/10000 for _ in range(0, ran)])

    x = np.arange(10000) / 100
    print(len(l_p0hat))
    plt.plot(l_p0hat, '-', label='p0hat', markersize=0.1, linewidth=1)
    plt.plot(l_p1hat, '-', label='p1hat', markersize=0.1, linewidth=1)
    plt.legend()
    #print(f'p0_hat={p0h_cnt/(10000)}, p1_hat={p1h_cnt/(10000)}')


if __name__ == '__main__':
    ana()
    sim()
    plt.show()