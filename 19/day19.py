#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 19
def get_year(): return 2019

def get(v, digs):
    s = str(digs[v])
    s = '0'*(5 - len(s)) + s
    op = digs[v]%100
    p1 = int(s[-3])
    p2 = int(s[-4])
    p3 = int(s[-5])
    return p3, p2, p1, op

def getV(v, mode, digs, rb):
    if mode == 1: return v
    elif mode == 0: return digs[v]
    else: return digs[v+rb]

def run_prog(digs, inp, out):
    D = defaultdict(int)
    L = len(digs)
    for i, x in enumerate(digs):
        D[i] = x
    digs = D

    i = 0
    rb = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    while i < L:
        C, B, A, op = get(i, digs)
        if op == 99: break
        elif op == 1:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            digs[c + (rb if C==2 else 0)] = getV(a, A, digs, rb) + getV(b, B, digs, rb)
        elif op == 2:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            digs[c+ (rb if C==2 else 0)] = getV(a, A, digs, rb) * getV(b, B, digs, rb)
        elif op == 3:
            a = digs[i+1]
            digs[a+ (rb if A==2 else 0)] = next(inp)
            FST = True
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            out.append(o)
        elif op == 5:
            a, b = digs[i+1], digs[i+2]
            if getV(a, A, digs, rb):
                i = getV(b, B, digs, rb)
                continue
        elif op == 6:
            a, b = digs[i+1], digs[i+2]
            if getV(a, A, digs, rb) == 0:
                i = getV(b, B, digs, rb)
                continue
        elif op == 7:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            VAL = int(getV(a, A, digs, rb) < getV(b, B, digs, rb))
            digs[c+ (rb if C==2 else 0)] = VAL
        elif op == 8:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            VAL = int(getV(a, A, digs, rb) == getV(b, B, digs, rb))
            digs[c+ (rb if C==2 else 0)] = VAL
        elif op == 9:
            a = digs[i+1]
            rb += getV(a, A, digs, rb)
            
        else:
            print('wtf, op: {} ip: {}'.format(op, i))
            return
        i += inc[op]

cache = {}
def has(x, y):
    if (x, y) in cache:
        return cache[x, y]
    itr = (c for c in [x, y])
    out = []
    run_prog(ints, itr, out)
    cache[(x, y)] = out[-1]
    return out[-1]

def p1(v):
    global ints
    ints = [int(x) for x in v.split(',')]
    C = 0
    for x in range(50):
        for y in range(50):
            C += has(x, y)
    return C


def p2(v):
    global ints
    ints = [int(x) for x in v.split(',')]
    pulled = 0

    x = 50
    best = 10**10, 0, 0
    last_first = 0
    while x + last_first < best[0]:
        y = last_first
        while True:
            if has(x, y): break
            y += 1
        last_first = y
        while has(x, y) or has(x-1, y):
            ok = True
            if best[0] <= x + y:
                y+=1
                continue
            for x2 in range(x, x + 100):
                for y2 in range(y, y + 100):
                    if not has(x2, y2):
                        ok = False
                        break
                if not ok: break
            if ok: 
                best = abs(x) + abs(y), x, y
            y += 1
        x += 1
    x, y = best[1:]
    return x*10000 + y


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
