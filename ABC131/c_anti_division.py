# https://atcoder.jp/contests/abc131/tasks/abc131_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c,d=map(int,input().split())
    from fractions import gcd
    L=c*d//gcd(c,d)
    M=b-(b//c)-(b//d)+(b//L)
    m=a-1-((a-1)//c)-((a-1)//d)+((a-1)//L)
    print(M-m)
resolve()
