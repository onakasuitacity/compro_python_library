# https://atcoder.jp/contests/agc020/tasks/agc020_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    print("Alice" if((a+b)&1==0) else "Borys")
resolve()
