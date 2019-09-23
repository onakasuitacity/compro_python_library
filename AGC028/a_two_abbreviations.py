# https://atcoder.jp/contests/agc028/tasks/agc028_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from fractions import gcd
    n,m=map(int,input().split())
    s,t=[input() for _ in range(2)]
    gcd=gcd(n,m)
    lcm=n*m//gcd
    n//=gcd
    m//=gcd
    print(lcm if all(s[n*i]==t[m*i] for i in range(gcd)) else -1)
resolve()
