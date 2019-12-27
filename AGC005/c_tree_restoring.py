# https://atcoder.jp/contests/agc005/tasks/agc005_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    D=defaultdict(int)
    for a in A: D[a]+=1

    m=max(A)
    B=list(range(m//2+1,m+1))*2
    if(m&1==0): B.append(m//2)

    for b in B:
        if(D[b]==0):
            print("Impossible")
            return
        D[b]-=1

    s=min(B)
    for key,val in D.items():
        if(val==0): continue
        if(not (s+1<=key<=m)):
            print("Impossible")
            return

    print("Possible")
resolve()
