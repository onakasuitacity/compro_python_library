# https://atcoder.jp/contests/agc026/tasks/agc026_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict

def resolve():
    n=int(input())
    S=input()
    S,T=S[:n],S[2*n-1:n-1:-1]
    
    C=defaultdict(int)
    for V in range(1<<n):
        s=''.join([s if((V>>i)&1) else '' for i,s in enumerate(S)])
        t=''.join([s if(not (V>>i)&1) else '' for i,s in enumerate(S)])
        C[(s,t)]+=1

    ans=0
    for V in range(1<<n):
        s=''.join([t if((V>>i)&1) else '' for i,t in enumerate(T)])
        t=''.join([t if(not (V>>i)&1) else '' for i,t in enumerate(T)])
        ans+=C[(s,t)]

    print(ans)
resolve()
