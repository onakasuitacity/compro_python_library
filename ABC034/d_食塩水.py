# https://atcoder.jp/contests/abc034/submissions/me
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    W=[0]*n; P=[0]*n
    for i in range(n):
        w,p=map(int,input().split())
        W[i]=w; P[i]=p
    l,r=0,100
    while(r-l>10**-10):
        h=(l+r)/2
        T=[W[i]*(P[i]-h) for i in range(n)]
        T.sort()
        s=sum(T[-k:])
        if s>0: l=h
        elif s<0: r=h
        else: break
    print(h)
resolve()
