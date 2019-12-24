#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 23
def get_year(): return 2019

def get(v, digs):
    s = str(digs[v])
    s = '0'*(5 - len(s)) + s
    op = digs[v]%100
    p1 = int(s[-3])
    p2 = int(s[-4])
    p3 = int(s[-5])
    return p3, p2, p1, op

def run_pipe(i, prog, q_in, qs, nat_q):
    out = []
    for c in run_prog(prog, q_in, nat_q, i):
        out.append(c)
        #print('output', i, c)
        if len(out)%3 == 0:
            if out[-3] == 255:
                nat_q.put(('packet', (out[-2], out[-1])))
            else:
                qs[out[-3]].put(out[-2])
                qs[out[-3]].put(out[-1])

def run_nat1(nat_q, q0):
    while True:
        cmd, v = nat_q.get()
        if cmd == 'packet':
            x, y = v
            return y

def run_nat2(nat_q, q0):
    x, y = -1, -1
    idle = [0]*50
    put = []
    got_data = False
    while True:
        cmd, v = nat_q.get()
        if cmd == 'packet':
            x, y = v
            got_data = True
        elif cmd == 'idle':
            idle[v] += 1
        elif cmd == 'active':
            idle = [0]*50
        if got_data and min(idle) > 3:
            got_data = False
            if put and y == put[-1]:
                return y
            put.append(y)
            q0.put(x)
            q0.put(y)

def getV(v, mode, digs, rb):
    if mode == 1: return v
    elif mode == 0: return digs[v]
    else: return digs[v+rb]

def run_prog(digs, q_in, nat_q, me_id):
    D = defaultdict(int)
    L = len(digs)
    for i, x in enumerate(digs):
        D[i] = x
    digs = D
    i = 0
    rb = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    idle = False
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
            try:
                inp = q_in.get(timeout=0.01)
            except Empty:
                inp = -1
            if inp == 'quit':
                return
            idle = inp == -1
            if idle:
                nat_q.put(('idle', me_id))
            else:
                nat_q.put(('active', me_id))
            digs[a+ (rb if A==2 else 0)] = inp
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            yield o
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
            break
        i += inc[op]

try:
    from queue import Empty, Queue
except:
    from Queue import Empty, Queue

from threading import Thread
def p1(v):
    ints = [int(x) for x in v.split(',')]
    qs = [Queue() for _ in range(50)]
    for i in range(50):
        qs[i].put(i)
    nat_q = Queue()
    ts = []
    for i in range(50):
    	ts.append(Thread(target=run_pipe, args=(i, ints, qs[i], qs, nat_q)))
    for t in ts:
        t.start()

    Y = run_nat1(nat_q, qs[0])
    for q in qs:
        q.put('quit')

    return Y

def p2(v):
    ints = [int(x) for x in v.split(',')]
    qs = [Queue() for _ in range(50)]
    for i in range(50):
        qs[i].put(i)
    nat_q = Queue()
    ts = []
    for i in range(50):
    	ts.append(Thread(target=run_pipe, args=(i, ints, qs[i], qs, nat_q)))
    for t in ts:
        t.start()
    Y = run_nat2(nat_q, qs[0])
    for q in qs:
        q.put('quit')
    return Y


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
