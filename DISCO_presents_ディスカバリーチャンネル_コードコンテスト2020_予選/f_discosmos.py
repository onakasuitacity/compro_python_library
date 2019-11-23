# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from fractions import gcd
def resolve():
    h,w,t=map(int,input().split())
    g1=gcd(h,t)
    g2=gcd(w,t)
    h=h//g1
    w=w//g2
    ans=pow(2,h,MOD)+pow(2,w,MOD)+pow(2,gcd(h,w),MOD)-3
    ans%=MOD
    print(pow(ans,g1*g2,MOD))
resolve()
