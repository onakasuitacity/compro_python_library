# https://atcoder.jp/contests/abc086/tasks/abc086_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=input().split()
    n=int(a+b)
    k=n**.5
    print("Yes" if(k==int(k)) else "No")
resolve()
