# https://atcoder.jp/contests/pakencamp-2019-day4/tasks/pakencamp_2019_day4_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    l1,r1=map(int,input().split())
    l2,r2=map(int,input().split())
    l3,r3=map(int,input().split())

    p1=1/(r1-l1+1)
    p2=1/(r2-l2+1)
    p3=1/(r3-l3+1)
    ans=0
    for i in range(l1,r1+1):
        R2=max(0,r2-max(l2,i+1)+1)
        R3=max(0,r3-max(l3,i+1)+1)
        ans+=R2*p2*R3*p3

    print(ans*p1)
resolve()
