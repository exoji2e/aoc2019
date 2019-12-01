#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from main import run
def get_day(): return datetime.date.today().day
def get_year(): return 2019

def p1(v):
    lines = v.strip().split('\n')
    return 0

def p2(v):
    lines = v.strip().split('\n')
    return 0


if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, D=True)
