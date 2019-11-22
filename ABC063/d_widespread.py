# https://atcoder.jp/contests/abc063/tasks/arc075_b
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

from math import ceil

def resolve():
    n,a,b=map(int,input().split())
    a=a-b
    H=[int(input()) for _ in range(n)]

    def check(x):
        cnt=0
        for i in range(n):
            cnt+=ceil(max(0,H[i]-b*x)/a)
        return cnt<=x

    print(bisection(0,max(H),check,left=False))
resolve()
