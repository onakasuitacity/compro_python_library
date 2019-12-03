# https://atcoder.jp/contests/abc022/tasks/abc022_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    Z=[None]*n
    W=[None]*n
    for i in range(n):
        x,y=map(int,input().split())
        Z[i]=x+y*1j
    for i in range(n):
        x,y=map(int,input().split())
        W[i]=x+y*1j

    mz=sum(Z)/n
    mw=sum(W)/n
    z0=max(abs(z-mz) for z in Z)
    w0=max(abs(w-mw) for w in W)
    print(w0/z0)
resolve()
