# https://atcoder.jp/contests/arc004/tasks/arc004_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    D=[int(input()) for _ in range(n)]
    m=max(D); S=sum(D)
    print(S)
    print(max(0,2*m-S))
resolve()
