# https://atcoder.jp/contests/abc148/tasks/abc148_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from fractions import gcd
def resolve():
    a,b=map(int,input().split())
    print(a*b//gcd(a,b))
resolve()
