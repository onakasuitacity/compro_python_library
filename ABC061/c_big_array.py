# https://atcoder.jp/contests/abc061/tasks/abc061_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    AB.sort()
    for a,b in AB:
        k-=b
        if(k<=0):
            print(a)
            return
resolve()
