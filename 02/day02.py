#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 2
def get_year(): return 2019

def p1(v):
    digs = [int(x) for x in v.split(',')]
    return run_prog(digs, 12, 2)

    return digs[0]

def run_prog(digs, i, j):
    digs[1] = i
    digs[2] = j
    ip = 0
    while ip < len(digs)-3:
        op, a, b, c = digs[ip:ip + 4]
        if op == 99: break
        elif op == 1:
            digs[c] = digs[a] + digs[b]
        elif op == 2:
            digs[c] = digs[a] * digs[b]
        else:
            print('wtf, op: {}'.format(op))
            return
        ip += 4
    return digs[0]


def p2(v):
    digs = [int(x) for x in v.split(',')]
    for i in range(10000):
        x = run_prog(list(digs), i//100, i%100)
        if x == 19690720:
            return i
    return 0


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
