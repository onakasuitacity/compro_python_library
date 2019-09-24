# https://atcoder.jp/contests/arc004/tasks/arc004_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import combinations
    n=int(input())
    A=[tuple(map(int,input().split())) for _ in range(n)]
    C=combinations(A,2)
    ans=0
    for u,v in C:
        ans=max(ans,(u[0]-v[0])**2+(u[1]-v[1])**2)
    print(ans**.5)
resolve()
