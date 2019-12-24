#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 17
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
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            out.append(o)
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

def get_grid(v):
    ints = [int(x) for x in v.split(',')]
    out = []
    run_prog(ints, [], out)
    grid = [[]]
    for o in out:
        if o == 10:
            grid.append([])
        else:
            grid[-1].append(chr(o))
    grid.pop()
    return grid

def get_ABC(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                x = i
                y = j

    D = (-1, 0)
    R = {(-1,0):(0, 1), (0, 1):(1, 0), (1, 0):(0, -1), (0, -1):(-1, 0)}
    L = {v:k for k, v in R.items()}
    path = []

    def ok(x, y, D):
        nx, ny = x + D[0], y + D[1]
        return 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and grid[nx][ny] == '#'

    while True:
        if ok(x, y, D):
            path[-1] += 1
        elif ok(x, y, L[D]):
            path.append('L')
            path.append(1)
            D = L[D]
        elif ok(x, y, R[D]):
            path.append('R')
            path.append(1)
            D = R[D]
        else:
            break
        x, y = x + D[0], y + D[1]
    path = [str(w) for w in path]
    S = ','.join(map(str, path))
    for a_e in range(1, len(path)):
        A = ','.join(path[:a_e])
        for b_s in range(a_e, len(path), a_e):
            for b_e in range(b_s+1, len(path)):
                B = ','.join(path[b_s:b_e])
                if len(B) > 20: continue
                S_RM = S.replace(A,'').replace(B, '')
                S_RM2 = [w for w in S_RM.split(',') if w]
                for i in range(1, len(S_RM2)+1):
                    no = len(S_RM2)//i
                    C_L = S_RM2[:i]
                    if not all(C_L[j%i] == S_RM2[j] for j in range(len(S_RM2))): continue
                    C = ','.join(S_RM2[:i])
                    MAIN = S.replace(A,'A').replace(B,'B').replace(C, 'C')
                    if max(map(len,[A,B,C,MAIN])) <= 20 and len(set(MAIN)) == 4:
                        return A, B, C, MAIN

def p1(v):
    grid = get_grid(v)
    s = 0
    for i in range(1, len(grid)-2):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == '^':
                x = i
                y = j
            if grid[i][j] != '#': continue
            if grid[i-1][j] != '#': continue
            if grid[i+1][j] != '#': continue
            if grid[i][j-1] != '#': continue
            if grid[i][j+1] != '#': continue
            s += i*j
    return s

def p2(v):
    A, B, C, S = get_ABC(get_grid(v))
    ints = [int(x) for x in v.split(',')]
    ints[0] = 2

    inp = (ord(c) for c in '\n'.join([S,A,B,C,'n','']))
    out = []
    run_prog(ints, inp, out)
    return out[-1]


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
