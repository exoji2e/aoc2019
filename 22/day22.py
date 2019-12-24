#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 22
def get_year(): return 2019

def sim1(deck, lines):
    MOD = len(deck)
    for line in lines:
        if line == 'deal into new stack':
            deck = deck[::-1]
        elif 'increment' in line:
            inc = int(line.split()[-1])
            new_deck = [-1]*MOD
            for i in range(MOD):
                new_deck[(i*inc)%MOD] = deck[i]
            deck = new_deck
        elif 'cut' in line:
            sz = int(line.split()[-1])
            deck = deck[sz:] + deck[0:sz]
                
        else:
            print('wtf: ', line)
        #print(deck)
    return deck

def p1(v):
    lines = v.strip().split('\n')
    deck = list(range(10007))
    deck = sim1(deck, lines)
    return next(i for i, v in enumerate(deck) if v == 2019)

def inv(a, MOD):
    return xgcd(a, MOD)[1]

# returns g = gcd(a, b), x0, y0, 
# where g = x0*a + y0*b
def xgcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = (a // b, b, a % b)
        x0, x1 = (x1, x0 - q * x1)
        y0, y1 = (y1, y0 - q * y1)
    return (a, x0, y0)

def sim2(P, MOD, lines):
    for line in lines[::-1]:
        if line == 'deal into new stack':
            P = MOD - P - 1
        elif 'increment' in line:
            inc = int(line.split()[-1])
            P = (P*inv(inc, MOD))%MOD
        elif 'cut' in line:
            sz = int(line.split()[-1])%MOD
            P = (P+sz)%MOD
        else:
            print('wtf: ', line)
    return P

def apply2(k, m, MOD):
    #(k*(k*P + m) + m)%MOD
    #k*k, m*k + m
    return k*k%MOD, (k+1)*m%MOD

def applyX(X, lines, MOD, P):
    for _ in range(X):
        P = sim2(P, MOD, lines)
    return P

def p2(v):
    lines = v.strip().split('\n')
    P = 2020
    MOD = 119315717514047
    x = sim2(P, MOD, lines)
    P0 = sim2(0, MOD, lines)
    P1 = sim2(1, MOD, lines)
    P1 = (P1 - P0)%MOD
    times = 101741582076661
    P = 2020
    #res = applyX(times, lines, MOD, P)
    no = 0
    while (1<<no) <= times:
        if (1<<no) & times:
            P = (P*P1 + P0)%MOD
        P1, P0 = apply2(P1, P0, MOD)
        no += 1
    return P #, res
    
if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
