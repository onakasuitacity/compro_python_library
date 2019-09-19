# https://atcoder.jp/contests/abc096/tasks/abc096_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c=map(int,input().split())
    k=int(input())
    print((2**k-1)*max(a,b,c)+a+b+c)
resolve()
