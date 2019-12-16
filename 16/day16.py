#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 16
def get_year(): return 2019

def fft(digs, offSet):
    for lap in range(100):
        new = [0]*len(digs)
        pref = [0]
        for c in digs:
            pref.append(pref[-1] + c)
        for i in range(offSet, len(digs)):
            S = 0
            R = 0
            L = (i+1)*4
            sz = len(pref) - 1
            for no in range((len(digs)+L-1)//L):
                a = no*L + 1*(i+1) - 1
                b = no*L + 2*(i+1) - 1
                c = no*L + 3*(i+1) - 1
                d = no*L + 4*(i+1) - 1
                R += pref[min(sz, b)]  - pref[min(sz, a)]
                R -= pref[min(sz, d)]  - pref[min(sz, c)]
            new[i] = (int(str(R)[-1]))
        digs = new
    return digs


def p1(v):
    digs = [int(c) for c in v.strip()]
    gen = fft(digs, 0)
    return ''.join(map(str,digs[:8]))

def p2(v):
    digs = [int(c) for c in v.strip()]
    offSet = int(''.join(map(str, digs[:7])))
    V = list(digs)
    digs = []
    for _ in range(10000):
        for d in V:
            digs.append(d)
    out = fft(digs, offSet)
    return ''.join(map(str, out[offSet:8+offSet]))


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
