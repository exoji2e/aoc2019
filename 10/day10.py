#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 10
def get_year(): return 2019

def coords(lines):
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '#':
                yield x, y

def gcd(a, b):
    return gcd(b, a%b) if b else a
import math

def center(v):
    lines = v.strip().split('\n')
    ast = set()
    for x, y in coords(lines):
        ast.add((x, y))
    best = 0, 0, 0
    V = []
    for x, y in ast:
        tot = 0
        for x_t, y_t in ast:
            if (x, y) == (x_t, y_t):
                continue
            fail = False
            dx, dy = x_t - x, y_t - y
            g = gcd(abs(dx), abs(dy))
            jmp_x, jmp_y = dx//g, dy//g
            for i in range(1, g):
                X = x + jmp_x*i
                Y = y + jmp_y*i
                if (X, Y) in ast:
                    fail = True
            if not fail: 
                tot += 1
        best = max(best, (tot, x, y))
    return best

def p1(v):
    return center(v)[0]

def p2(v):
    lines = v.strip().split('\n')
    ast = set()
    for x, y in coords(lines):
        ast.add((x, y))
    best = center(v)
    x, y = best[1], best[2]
    V = []
    for x_t, y_t in ast:
        if (x, y) == (x_t, y_t):
            continue
        fail = 0
        dx, dy = x_t - x, y_t - y
        g = gcd(abs(dx), abs(dy))
        jmp_x, jmp_y = dx//g, dy//g
        for i in range(1, g):
            X = x + jmp_x*i
            Y = y + jmp_y*i
            if (X, Y) in ast:
                fail += 1
        DX = dy
        DY = dx
        ang = (math.atan2(DX, -DY))%(math.pi*2)
        V.append((fail, ang, x_t, y_t))
    V.sort()
    _, _, x, y = V[199]
    return x + y*100


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
