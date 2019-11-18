# https://atcoder.jp/contests/abc050/tasks/abc050_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    T=list(map(int,input().split()))
    s=sum(T)
    m=int(input())
    PX=[tuple(map(int,input().split())) for _ in range(m)]
    for i in range(m):
        p,x=PX[i]
        p-=1
        print(s-T[p]+x)
resolve()
