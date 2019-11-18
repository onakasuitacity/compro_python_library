# https://atcoder.jp/contests/abc096/tasks/abc096_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def prime(n):
    if n<=1: return []
    S=[1]*(n+1)
    S[0]=0; S[1]=0
    for i in range(2,n):
        if S[i]==0: continue
        for j in range(2*i,n+1,i):
            S[j]=0
    return [p for p in range(n+1) if S[p]]

def resolve():
    n=int(input())
    P=prime(55555)
    S=set()
    for p in P:
        if(p%5==1): S.add(p)
    print(*list(S)[:n])
resolve()
