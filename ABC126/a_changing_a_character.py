# https://atcoder.jp/contests/abc126/tasks/abc126_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,k=map(int,input().split())
    s=input()
    print(s[:k-1]+s[k-1].lower()+s[k:])

resolve()
