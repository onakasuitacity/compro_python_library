# https://atcoder.jp/contests/abc101/tasks/arc099_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from math import log10

def f(x):
    s=sum(int(c) for c in str(x))
    return x/s

def next(x):
    d=int(log10(x))
    A=list(str(x))
    res=-1
    score=INF
    for i in range(d,-1,-1):
        A[i]='9'
        tmp=int(''.join(A))
        if(score>f(tmp)):
            score=f(tmp)
            res=tmp
    return res

def resolve():
    k=int(input())
    if(k<10):
        for i in range(1,k+1):
            print(i)
        return
    for i in range(1,10):
        print(i)
    k-=9
    now=9
    for _ in range(k):
        now=next(now+1)
        print(now)
resolve()
