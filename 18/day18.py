#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
from heapq import *

def get_day(): return 18
def get_year(): return 2019


def solve(crds):
    pq = []
    dist = {}
    def add(crds, ok, cost):
        T = tuple(crds), ok
        if T in dist and dist[T] <= cost: return
        dist[T] = cost
        heappush(pq, (cost, T))
    add(crds, 0, 0)
    while pq:
        cost, (crds, ok) = heappop(pq)
        if dist[crds, ok] < cost: continue
        crds = list(crds)
        if ok == 2**26 - 1: return cost
        for i in range(len(crds)):
            orig_c = crds[i]
            for (xx, yy), w in options(orig_c, ok):
                c = grid[xx][yy]
                v = ord(c) - ord('a')
                ok2 = ok | 1<<v
                crds[i] = (xx, yy)
                add(crds, ok2, w + cost)
            crds[i] = orig_c

def options(pt, ok):
    def inOK(diff):
        if diff < 0: return False
        return ok & 1<<diff

    def valid(C):
        return C in '.@' or ord('a') <= ord(C) <= ord('z') or inOK(ord(C) - ord('A'))
    q = [pt]
    vis = {pt: 0}
    while q:
        q2 = []
        for x, y in q:
            c = grid[x][y]
            if 'a' <= c <= 'z' and not inOK(ord(c)-ord('a')): continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(grid) and 0 <= ny < len(grid[nx])): continue
                C = grid[nx][ny]
                if (nx, ny) not in vis and valid(C):
                    vis[nx, ny] = vis[x,y] + 1
                    q2.append((nx, ny))
        q = q2
    out = []
    for i in range(26):
        c = chr(ord('a') + i)
        if not inOK(i) and LAST[c] in vis:
            out.append((LAST[c], vis[LAST[c]]))
    return out

LAST = {}
def find_at():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            LAST[grid[i][j]] = (i, j)
    return LAST['@']

def p1(v):
    lines = [list(s) for s in v.strip().split('\n')]
    global DP, grid
    DP, grid = {}, lines
    sx, sy = find_at()
    return solve([(sx, sy)])

def p2(v):
    lines = [list(s) for s in v.strip().split('\n')]
    global DP, grid
    DP, grid = {}, lines
    sx, sy = find_at()
    crds = [(sx+1, sy+1), (sx-1, sy+1), (sx+1, sy-1), (sx-1, sy-1)]
    for x, y in crds:
        lines[x][y] = '#'

    return solve(crds)


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, run_samples=False)
