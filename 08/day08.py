#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 8
def get_year(): return 2019

def p1(v):
    X = [int(c) for c in v.strip()]
    best = (10**10, -1)
    for i in range(0, len(v), 6*25):
        sub = v[i:i+6*25]
        zeros = sub.count('0')
        ones = sub.count('1')
        twos = sub.count('2')
        best = min(best, (zeros, ones*twos))

    return best[1]

def p2(v):
    subs = []
    for i in range(0, len(v), 6*25):
        sub = v[i:i+6*25]
        subs.append(sub)
    place = [2]*(6*25)
    for sub in subs:
        for i in range(6*25):
            if place[i] == 2 and sub[i] != '2':
                place[i] = sub[i]

    
    x = ''.join(place).replace('1','#').replace('0', '.')
    out = [''] + [x[i*25:(i+1)*25] for i in range(6)]


    return '\n'.join(out)


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
