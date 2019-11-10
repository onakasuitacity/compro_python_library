# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_h
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    for _ in range(n):
        a,b=map(int,input().split())
        if(a==b): print(-1)
        else: print(abs(a-b))
resolve()
