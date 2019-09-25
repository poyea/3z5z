import math as m
from scipy.stats import expon as e

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
    for t in range(0,10001):
        if t == 0:
            continue
    print(f'p0={p0(t*0.01)}, p1={p1(t*0.01)}')


def sim():
    state = 0
    p0h_cnt = 0
    p1h_cnt = 0
    t = 0
    while t < 10001:
        if state == 0:
            state = 1
            t += int(e.rvs(1/lam))
            p0h_cnt += int(e.rvs(1/lam))
        else:
            state = 0
            t += int(e.rvs(1/mu))
            p1h_cnt += int(e.rvs(1/mu))
    print(f'p0_hat={p0h_cnt/(10000)}, p1_hat={p1h_cnt/(10000)}')


if __name__ == '__main__':
    ana()
    sim()
