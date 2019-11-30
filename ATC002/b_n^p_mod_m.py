# https://atcoder.jp/contests/atc002/tasks/atc002_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,p=map(int,input().split())
    print(pow(n,p,m))
resolve()
