#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 6
def get_year(): return 2019

def p1(v):
    lines = v.strip().split('\n')
    tree = {}
    c = 0
    for line in lines:
        a, b = line.split(')')
        tree[b] = a
    for line in lines:
        a, b = line.split(')')
        x = b
        while x in tree:
            x = tree[x]
            c += 1
    return c

def p2(v):
    lines = v.strip().split('\n')
    d = defaultdict(list)
    tree = {}
    for line in lines:
        a, b = line.split(')')
        tree[b] = a
        d[a].append(b)
        d[b].append(a)

    S = tree['YOU']
    T = tree['SAN']
    q = [S]
    vis = set(q)
    c = 1
    while q:
        q2 = []
        for u in q:
            for v in d[u]:
                if v == T:
                    return c
                if v not in vis:
                    vis.add(v)
                    q2.append(v)
        q = q2
        c += 1

    return None


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
