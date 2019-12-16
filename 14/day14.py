#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 14
def get_year(): return 2019

def get_order(lines):
    def grep(lines, done, j):
        x = []
        for i, line in enumerate(lines):
            if i == j or done[i]: continue
            x.append(line)
        return '\n'.join(x)
    
    order = []
    done = [0]*len(lines)
    ch = True
    while ch:
        ch = False
        for i, line in enumerate(lines):
            v, X = line.split('=>')[1].strip().split()
            v = int(v)
            if not done[i] and X not in grep(lines, done, i):
                done[i] = True
                order.append(i)
                ch = True
                break
    return order

def needed(S, order, lines):
    need = Counter()
    need['FUEL'] = S
    for i in order:
        v, X = lines[i].split('=>')[1].strip().split()
        v = int(v)
        c = need[X]
        no = (c + v - 1)//v
        other = lines[i].split('=>')[0].strip().split(', ')
        for o in other:
            a, b = o.split()
            a = int(a)
            need[b] += a*no
        del need[X]
    return need['ORE']

def p1(v):
    lines = v.strip().split('\n')
    return needed(1, get_order(lines), lines)

def p2(v):
    lines = v.strip().split('\n')
    order = get_order(lines)
    lo = 0
    hi = 10**12
    while lo < hi:
        mid = (lo + hi + 1)//2
        if needed(mid, order, lines) < 10**12:
            lo = mid
        else:
            hi = mid - 1

    return lo


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
