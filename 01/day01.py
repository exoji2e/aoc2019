import sys, time
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return 1
def get_year(): return 2019
def p1(v, log=False):
    ws = map(int, v.split('\n'))
    tot = 0
    for c in ws:
        tot += c//3 - 2
    return tot

def p2(v, log=False):
    ws = map(int, v.split('\n'))
    tot = 0
    for c in ws:
        x = c//3 - 2
        while x > 0:
            tot += x
            x = x//3 - 2
    return tot

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
