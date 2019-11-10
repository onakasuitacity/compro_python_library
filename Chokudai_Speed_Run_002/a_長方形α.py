# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    for _ in range(n):
        a,b=map(int,input().split())
        print(a*b)
resolve()
