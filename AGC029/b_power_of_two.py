# https://atcoder.jp/contests/agc029/tasks/agc029_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    D=defaultdict(int)
    for a in A:
        D[a]+=1

    A.sort(reverse=1)
    ans=0
    for a in A:
        if(D[a]==0): continue
        k=a.bit_length()
        d=(1<<k)-a
        if(a!=d):
            if(D[d]):
                ans+=1
                D[a]-=1
                D[d]-=1
        else:
            if(D[d]>=2):
                ans+=1
                D[d]-=2
    print(ans)
resolve()
