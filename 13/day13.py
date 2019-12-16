#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 13
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

def CMP(X, x):
    if X < x: return -1
    if X > x: return 1
    return 0

def run_prog(digs, out):
    D = defaultdict(int)
    L = len(digs)
    for i, x in enumerate(digs):
        D[i] = x
    digs = D

    X, Y = 0, 0
    x = 18
    no = 0
    i = 0
    rb = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    nxt = 17
    id_t = 0
    sz = 0
    while i < L:
        C, B, A, op = get(i, digs)
        if op == 99: break
        elif op == 1:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            idx = c + (rb if C==2 else 0)
            if idx == 386:
                pass#print(a, b)
            digs[idx] = getV(a, A, digs, rb) + getV(b, B, digs, rb)
        elif op == 2:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            digs[c+ (rb if C==2 else 0)] = getV(a, A, digs, rb) * getV(b, B, digs, rb)
        elif op == 3:
            a = digs[i+1]
            DIR = CMP(nxt, x)
            #if DIR == 0: id_t += 1
            x += DIR
            digs[a+ (rb if A==2 else 0)] = DIR
            #FST = True
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            if no%3 == 0:
                X = o
            elif no%3 == 1:
                Y = o
            else:
                out.append((X, Y, o, x))
                if o == 4:
                    nxt = X
                sz += 1
                if X == -1:
                    last_out = o
            no += 1
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
    return last_out

def p1(v):
    ints = [int(x) for x in v.split(',')]
    out = []
    run_prog(ints, out)
    S = set()
    for y, x, z, _ in out:
        if z == 2: S.add((x,y))
    return len(S)

def p2(v):
    lines = v.strip().split('\n')
    ints = [int(x) for x in v.split(',')]
    ints[0] = 2
    out = []
    #inp = (i for i in [1] + [0]*100)
    return run_prog(ints, out)

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
