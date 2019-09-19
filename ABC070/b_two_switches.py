# https://atcoder.jp/contests/abc070/tasks/abc070_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c,d=map(int,input().split())
    print(max(0,min(d,b)-max(a,c)))
resolve()
