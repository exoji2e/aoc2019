#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 12
def get_year(): return 2019

def CMP(x, x2):
    if x == x2: return 0
    if x < x2: return 1
    if x > x2: return -1

def update(planets, step=100):
    p_out = []
    for x, y, z, vx, vy, vz in planets:
        dvx, dvy, dvz = 0, 0, 0
        for x2, y2, z2, _, _, _ in planets:
            
            dvx += CMP(x, x2) 
            dvy += CMP(y, y2) 
            dvz += CMP(z, z2) 
        vx += dvx
        vy += dvy
        vz += dvz

        x, y, z = x + vx, y+vy, z+vz
        p_out.append((x, y, z, vx, vy, vz))
    return p_out

def NRG(planets):
    tot = 0
    for x, y, z, vx, vy, vz in planets:
        tot += (abs(x) + abs(y) + abs(z))*(abs(vx) + abs(vy) + abs(vz))
    return tot

def p1(v):
    lines = v.strip().split('\n')
    planets = []
    for line in lines:
        line = line.replace(',','')
        line = line.replace('<','')
        line = line.replace('>','')
        line = line.replace('x','')
        line = line.replace('y','')
        line = line.replace('z','')
        line = line.replace('=','')
        x, y, z = map(int, line.split())
        planets.append((x, y, z, 0, 0, 0))

    for steps in range(1, 1001):
        planets = update(planets, steps)
    return NRG(planets)

def get(i, planets):
    return tuple([(p[i], p[i+3]) for p in planets])

def gcd(a, b): return gcd(b, a%b) if b else a

def lcm(a, b): return a*b//gcd(a, b)

def p2(v):
    lines = v.strip().split('\n')
    planets = []
    for line in lines:
        line = line.replace(',','')
        line = line.replace('<','')
        line = line.replace('>','')
        line = line.replace('x','')
        line = line.replace('y','')
        line = line.replace('z','')
        line = line.replace('=','')
        x, y, z = map(int, line.split())
        planets.append((x, y, z, 0, 0, 0))
    steps = 0
    X = {get(0, planets): 0}
    Y = {get(1, planets): 0}
    Z = {get(2, planets): 0}
    mx, my, mz = -1, -1, -1
    sx, sy, sz = None, None, None

    while min(mx, my, mz) == -1:
        steps += 1
        planets = update(planets)
        x = get(0, planets)
        if x in X and mx == -1:
            mx = steps
            sx = X[x]
        y = get(1, planets)
        if y in Y and my == -1:
            my = steps
            sy = Y[y]
        z = get(2, planets)
        if z in Z and mz == -1:
            mz = steps
            sz = Z[z]
        X[x] = steps
        Y[y] = steps
        Z[z] = steps
    assert sx == sy == sz
    return lcm(mx, lcm(my, mz))


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
