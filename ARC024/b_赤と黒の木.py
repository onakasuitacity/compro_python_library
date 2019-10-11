# https://atcoder.jp/contests/arc024/tasks/arc024_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    n=int(input())
    A=[int(input()) for _ in range(n)]
    A=groupby(A)
    B=[]
    for a in A:
        B.append(len(list(a[1])))
    k=max(B)
    if len(B)%2: k=max(k,B[0]+B[-1])
    print((k+1)//2 if len(B)!=1 else -1)
resolve()
