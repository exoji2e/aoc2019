#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
import queue
def get_day(): return 9
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


def run_pipe(i, prog, q_in, q_out, part1=False):
    x = run_prog(prog, q_in, q_out, part1=part1)
    if i == 4:
        BEST[0] = max(BEST[0], x)

def run_prog(digs, q_in, q_out):
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
            digs[a+ (rb if A==2 else 0)] = q_in.get()
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            q_out.put(o)
            last_out = o
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
    q_in = queue.Queue()
    q_out = queue.Queue()
    q_in.put(1)
    run_prog(ints, q_in, q_out)
    return q_out.get()

def p2(v):
    ints = [int(x) for x in v.split(',')]
    q_in = queue.Queue()
    q_out = queue.Queue()
    q_in.put(2)
    run_prog(ints, q_in, q_out)

    return q_out.get()


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
