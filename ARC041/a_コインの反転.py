# https://atcoder.jp/contests/arc041/tasks/arc041_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    x,y=map(int,input().split())
    k=int(input())
    if y>=k: print(x+k)
    else: print(x+y-(k-y))
resolve()
