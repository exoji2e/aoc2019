#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 24
def get_year(): return 2019

def ev(c):
    return c == '#'
def gen_empty():
    return [['.' for _ in range(5)] for _ in range(5)]

def toStr(g):
    return ''.join(''.join(line) for line in g)

def p1(v):
    lines = [list(line) for line in v.strip().split('\n')]
    def biodiv(grid):
        S = toStr(grid)
        return int(S.replace('#','1').replace('.', '0')[::-1], 2)

    def gennxt(grid):
        g2 = gen_empty()
        for i in range(5):
            for j in range(5):
                c = 0
                for a,b in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                    if 0 <= a < 5 and 0 <= b < 5:
                        c += grid[a][b] == '#'
                if c == 1 or (c == 2 and grid[i][j] == '.'):
                    g2[i][j] = '#'
        return g2
    last = set([biodiv(lines)])
    while True:
        lines = gennxt(lines)
        b = biodiv(lines)
        if b in last:
            return b
        last.add(b)

def p2(v):
    def gennext(grids):
        def cnt_y(l, x):
            c = 0
            for y in range(5): c += isSet(l, x, y)
            return c
        def cnt_x(l, y):
            c = 0
            for x in range(5): c += isSet(l, x, y)
            return c

        def isSet(l, x, y):
            return grids[l][x][y] == '#'
        def get_cnt(l, x, y):
            if x == 2 and y == 2: return 0
            c = 0
            for x2, y2 in [(x, y+1), (x, y -1), (x+1, y), (x-1, y)]:
                if x2 == 2 and y2 == 2:
                    if x == 1:   c += cnt_y(l + 1, 0)
                    elif x == 3: c += cnt_y(l + 1, 4)
                    elif y == 1: c += cnt_x(l + 1, 0)
                    elif y == 3: c += cnt_x(l + 1, 4)

                elif x2 < 0:  c += isSet(l - 1, 1, 2)
                elif y2 < 0:  c += isSet(l - 1, 2, 1)
                elif x2 == 5: c += isSet(l - 1, 3, 2)
                elif y2 == 5: c += isSet(l - 1, 2, 3)
                else:         c += isSet(l, x2, y2)
            return c
        def gen_layer(l):
            g = gen_empty()
            for x in range(5):
                for y in range(5):
                    c = get_cnt(l, x, y)
                    if c == 1 or (c == 2 and grids[l][x][y] == '.'):
                        g[x][y] = '#'
            return g

        g2 = defaultdict(gen_empty)
        min_l, max_l = 0,0
        for l in list(grids.keys()):
            g2[l] = gen_layer(l)
            min_l = min(min_l, l - 1)
            max_l = max(max_l, l + 1)
        
        min_g = gen_layer(min_l)
        max_g = gen_layer(max_l)
        if '#' in toStr(min_g):
            g2[min_l] = min_g
        if '#' in toStr(max_g):
            g2[max_l] = max_g
        return g2

    grid = [list(line) for line in v.strip().split('\n')]
    grids = defaultdict(gen_empty)
    grids[0] = grid

    for i in range(200):
        grids = gennext(grids)
    return ''.join(toStr(grid) for grid in grids.values()).count('#')

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
