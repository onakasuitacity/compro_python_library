# https://atcoder.jp/contests/agc019/tasks/agc019_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    A=input()
    n=len(A)
    ans=n*(n+1)//2

    D=defaultdict(int)
    for a in A:
        D[a]+=1

    for c in D.values():
        ans-=c*(c+1)//2

    print(ans+1)
resolve()
