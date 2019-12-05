#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 5
def get_year(): return 2019

def get(v, digs):
    s = str(digs[v])
    op = digs[v]%100
    p1 = 1 if len(s) > 2 and s[-3] == '1' else 0
    p2 = 1 if len(s) > 3 and s[-4] == '1' else 0
    p3 = 1 if len(s) > 4 and s[-5] == '1' else 0
    return p3, p2, p1, op

def getV(v, mode, digs):
    return v if mode else digs[v]

def run_prog(digs, inp):
    i = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4]
    while i < len(digs):
        C, B, A, op = get(i, digs)
        if op == 99: break
        elif op == 1:
            a, b, c = digs[i+1:i+4]
            digs[c] = getV(a, A, digs) + getV(b, B, digs)
        elif op == 2:
            a, b, c = digs[i+1:i+4]
            digs[c] = getV(a, A, digs) * getV(b, B, digs)
        elif op == 3:
            a = digs[i+1]
            digs[a] = next(inp)
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs)
            #print('op 4 @ {}: {}'.format(i, o))
            last_out = o
        elif op == 5:
            a, b = digs[i+1:i+3]
            if getV(a, A, digs):
                i = getV(b, B, digs)
                continue
        elif op == 6:
            a, b = digs[i+1:i+3]
            if getV(a, A, digs) == 0:
                i = getV(b, B, digs)
                continue
        elif op == 7:
            a, b, c = digs[i+1:i+4]
            VAL = int(getV(a, A, digs) < getV(b, B, digs))
            digs[c] = VAL
        elif op == 8:
            a, b, c = digs[i+1:i+4]
            VAL = int(getV(a, A, digs) == getV(b, B, digs))
            digs[c] = VAL
            
        else:
            print('wtf, op: {} ip: {}'.format(op, i))
            return
        i += inc[op]
    return last_out

def p1(v):
    lines = v.strip().split('\n')
    PROG = [int(ch) for ch in v.split(',')]
    inp = (1 for _ in range(1))
    return run_prog(PROG, inp)

def p2(v):
    lines = v.strip().split('\n')
    PROG = [int(ch) for ch in v.split(',')]
    inp = (5 for _ in range(1))
    return run_prog(PROG, inp)

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
