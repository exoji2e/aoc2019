#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 15
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

def backtrack(vis, S, T):
    last = T
    cnt = 0
    while T != S:
        last = T
        T = vis[T]
        cnt += 1
        if cnt == 1000:
            print('WTF', T, vis[T], S)
    return last


def get_dir(S, T, COL):
    q = [S]
    vis = {S:S}
    dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        q2 = []
        for x, y in q:
            for dx, dy in dd:
                n = dx + x, dy + y
                if n == T:
                    vis[n] = (x, y)
                    return backtrack(vis, S, T)
                if n in COL and COL[n] == 1 and n not in vis:
                    q2.append(n)
                    vis[n] = (x, y)
        q = q2

def get_dir_int(S, T):
    if S[0] > T[0]: return 3
    if S[0] < T[0]: return 4
    if S[1] < T[1]: return 2
    if S[1] > T[1]: return 1

                

def run_prog(digs):
    D = defaultdict(int)
    L = len(digs)
    for i, x in enumerate(digs):
        D[i] = x
    digs = D

    COL = {(0,0) : 1}
    q = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    P = 0, 0
    T = q.pop()

    i = 0
    rb = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    FST = None
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
            while T in COL:
                if len(q) == 0: return COL
                T = q.pop()
            N = get_dir(P, T, COL)
            digs[a+ (rb if A==2 else 0)] = get_dir_int(P, N)
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            if o == 1 or o == 2:
                P = N
                if N not in COL:
                    x, y = P
                    q.append((x, y+1))
                    q.append((x, y-1))
                    q.append((x+1, y))
                    q.append((x-1, y))
            COL[N] = o
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

def get_len(S, COL, part1=True):
    q = [S]
    vis = {S:S}
    dd = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    i = 0
    while q:
        q2 = []
        for x, y in q:
            for dx, dy in dd:
                n = dx + x, dy + y
                if n in COL and COL[n] == 2 and part1:
                    return i + 1
                if n in COL and COL[n] == 1 and n not in vis:
                    q2.append(n)
                    vis[n] = (x, y)
        q = q2
        i += 1
    return i - 1
def p1(v):
    ints = [int(x) for x in v.split(',')]
    COL = run_prog(ints)
    X = [(x, y) for (x, y), v in COL.items() if v == 2]

    return get_len((0, 0), COL)

# Inte 315 eller 316
def p2(v):
    ints = [int(x) for x in v.split(',')]
    COL = run_prog(ints)
    X = next((x, y) for (x, y), v in COL.items() if v == 2)
    return get_len(X, COL, False)


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
