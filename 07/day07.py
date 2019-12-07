#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 7
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

from threading import Thread
import queue
import itertools

def run_pipe(i, prog, q_in, q_out, part1=False):
    x = run_prog(prog, q_in, q_out, part1=part1)
    if i == 4:
        BEST[0] = max(BEST[0], x)

def run_prog(digs, q_in, q_out, part1=False):
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
            digs[a] = q_in.get()
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs)
            q_out.put(o)
            if part1: return o 
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
def gen(lst):
    return (i for i in lst)

BEST = [-1]

def p1(v):
    BEST[0] = -1
    PROG = [int(x) for x in v.split(',')]
    MAX = 0
    for inps in itertools.permutations(range(5)):
        qs = [queue.Queue() for i in range(5)]
        for i in range(5):
            qs[i].put(inps[i])
        qs[0].put(0)
        ts = [Thread(target=run_pipe, args=(i, list(PROG), qs[i], qs[(i+1)%5], True)) for i in range(5)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()

    return BEST[0]


def p2(v):
    BEST[0] = -1
    PROG = [int(x) for x in v.split(',')]
    MAX = 0
    for inps in itertools.permutations(range(5, 10)):
        qs = [queue.Queue() for i in range(5)]
        for i in range(5):
            qs[i].put(inps[i])
        qs[0].put(0)
        ts = [Thread(target=run_pipe, args=(i, list(PROG), qs[i], qs[(i+1)%5])) for i in range(5)]
        for t in ts: t.start()
        for t in ts: t.join()
    return BEST[0]


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
