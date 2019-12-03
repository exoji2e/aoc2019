#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return datetime.date.today().day
def get_year(): return 2019

def get_dxdy(c):
    if c == 'R': dx, dy = 1, 0
    if c == 'L': dx, dy = -1, 0
    if c == 'D': dx, dy = 0, 1
    if c == 'U': dx, dy = 0, -1
    return dx, dy

def walk_1(coords):
    X = set()
    x, y = 0, 0
    for w in coords.split(','):
        dx, dy = get_dxdy(w[0])
        no = int(w[1:])
        for _ in range(no):
            x, y = x+ dx, y + dy
            X.add((x, y))
    return X

def walk_2(coords):
    X = {}
    x, y, i = 0, 0, 0
    for w in coords.split(','):
        dx, dy = get_dxdy(w[0])
        no = int(w[1:])
        for _ in range(no):
            x, y = x+ dx, y + dy
            i += 1
            X[(x, y)] = i
    return X

def p1(v):
    lines = v.strip().split('\n')
    X = walk_1(lines[0])
    Y = walk_1(lines[1])
    inters = X&Y
    MIN = min(abs(x) + abs(y) for x, y in inters)
    return MIN

def p2(v):
    lines = v.strip().split('\n')
    X = walk_2(lines[0])
    Y = walk_2(lines[1])
    MIN = 10**10
    for T, c in X.items():
        if T in Y:
            d = Y[T]
            MIN = min(MIN, c + d)
    return MIN


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
