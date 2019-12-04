#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 4
def get_year(): return 2019

def p1(v):
    x, y = map(int, v.split('-'))
    c = 0
    for p in range(x, y+1):
        s = str(p)
        ss = ''.join(sorted(s))
        if s == ss and len(set(s)) < len(s):
            c += 1
    return c

def p2(v):
    x, y = map(int, v.split('-'))
    c = 0
    for p in range(x, y+1):
        s = str(p)
        ss = ''.join(sorted(s))
        cnt = set()
        for ch in s:
            cnt.add(s.count(ch))

        if s == ss and 2 in cnt:
            c += 1
    return c


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, D=True)
