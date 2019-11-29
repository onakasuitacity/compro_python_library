# https://atcoder.jp/contests/abc048/tasks/abc048_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,x=map(int,input().split())
    print(b//x-(a-1)//x)
resolve()
