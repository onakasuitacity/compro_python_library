# https://atcoder.jp/contests/abc146/tasks/abc146_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

from math import log10

def resolve():
    a,b,x=map(int,input().split())
    def check(n):
        return a*n+b*(int(log10(n))+1)<=x
    print(bisection(1,10**9,check))
resolve()
