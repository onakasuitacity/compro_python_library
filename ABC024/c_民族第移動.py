# https://atcoder.jp/contests/abc024/tasks/abc024_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,d,k=map(int,input().split())
    LR=[tuple(map(int,input().split())) for _ in range(d)]
    ST=[tuple(map(int,input().split())) for _ in range(k)]

    def calc(s,t):
        l=r=s
        day=1
        for L,R in LR:
            if(l<=L<=r or L<=l<=R):
                l=min(L,l)
                r=max(R,r)
            if(l<=t<=r):
                return day
            day+=1

    for s,t in ST:
        print(calc(s,t))
resolve()
