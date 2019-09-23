# https://atcoder.jp/contests/abc046/tasks/abc046_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    print(k*((k-1)**(n-1)))
resolve()
