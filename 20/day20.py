#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 20
def get_year(): return 2019

def p1(v):
    def isLetter(x, y):
        if x < len(lines) and y < len(lines[x]):
            return ord('A') <= ord(lines[x][y]) <= ord('Z')
        return False
    def isOK(x, y):
        if x < len(lines) and y < len(lines[x]):
            return lines[x][y] == '.'
    lines = [list(l) for l in v.split('\n')]
    pos = {}
    D = defaultdict(list)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if isLetter(x, y):
                if isLetter(x + 1, y):
                    pos[x+2, y] = lines[x][y] + lines[x+1][y]
                    pos[x-1, y] = lines[x][y] + lines[x+1][y]
                    pos[x+1, y] = lines[x][y] + lines[x+1][y]
                    pos[x, y] = lines[x][y] + lines[x+1][y]
                if isLetter(x, y+1):
                    pos[x, y+2] = lines[x][y] + lines[x][y+1]
                    pos[x, y-1] = lines[x][y] + lines[x][y+1]
                    pos[x, y+1] = lines[x][y] + lines[x][y+1]
                    pos[x, y] = lines[x][y] + lines[x][y+1]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if isLetter(x, y):
                if (x, y) not in pos:
                    print(x, y, lines[x][y])

    for k, v in pos.items():
        D[v].append(k)
    q = [k for k, v in pos.items() if v == 'AA']
    vis = set(q)
    i = 0
    while q:
        q2 = []
        for x, y in q:
            for (nx, ny) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if nx < 0 or ny < 0: continue
                if isOK(nx, ny) and (nx, ny) not in vis:
                    q2.append((nx, ny))
                    vis.add((nx, ny))
                if isLetter(nx, ny):
                    Lab = pos[nx, ny]
                    if Lab == 'ZZ':
                        return i
                    for x2, y2 in D[Lab]:
                        if (x2, y2) not in vis:
                            q2.append((x2, y2))
                            vis.add((x2, y2))
        i += 1
        q = q2



    
    return 0

def p2(v):
    def isLetter(x, y):
        if x < len(lines) and y < len(lines[x]):
            return ord('A') <= ord(lines[x][y]) <= ord('Z')
        return False
    def isOK(x, y):
        if x < len(lines) and y < len(lines[x]):
            return lines[x][y] == '.'
    lines = [list(l) for l in v.split('\n')]
    pos = {}
    D = defaultdict(list)
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if isLetter(x, y):
                if isLetter(x + 1, y):
                    pos[x+2, y] = lines[x][y] + lines[x+1][y]
                    pos[x-1, y] = lines[x][y] + lines[x+1][y]
                    pos[x+1, y] = lines[x][y] + lines[x+1][y]
                    pos[x, y] = lines[x][y] + lines[x+1][y]
                if isLetter(x, y+1):
                    pos[x, y+2] = lines[x][y] + lines[x][y+1]
                    pos[x, y-1] = lines[x][y] + lines[x][y+1]
                    pos[x, y+1] = lines[x][y] + lines[x][y+1]
                    pos[x, y] = lines[x][y] + lines[x][y+1]
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if isLetter(x, y):
                if (x, y) not in pos:
                    print(x, y, lines[x][y])

    for k, v in pos.items():
        D[v].append(k)
    q = [(k[0], k[1], 0) for k, v in pos.items() if v == 'AA']
    vis = set(q)
    i = 0
    while q:
        q2 = []
        for x, y, d in q:
            for (nx, ny) in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if nx < 0 or ny < 0: continue
                if isOK(nx, ny) and (nx, ny, d) not in vis:
                    q2.append((nx, ny, d))
                    vis.add((nx, ny, d))
                if isLetter(nx, ny):
                    Lab = pos[nx, ny]
                    outer = min(nx, ny) < 5 or nx >= len(lines) - 5  or ny >= len(lines[0]) - 5
                    if Lab == 'ZZ' and d == 0:
                        #print('ZZ, ', i)
                        return i
                    diff = 1 - outer*2
                    if d + diff < 0: continue
                    for x2, y2 in D[Lab]:
                        if abs(nx - x2) + abs(ny -y2) > 3:
                            if (x2, y2, d + diff) not in vis:
                                q2.append((x2, y2, d + diff))
                                vis.add((x2, y2, d + diff))
        i += 1
        q = q2


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
