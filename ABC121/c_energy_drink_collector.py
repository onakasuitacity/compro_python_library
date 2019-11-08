# https://atcoder.jp/contests/abc121/tasks/abc121_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    AB.sort()
    now=m
    score=0
    for a,b in AB:
        k=min(m,b)
        m-=k
        score+=a*k
        if(m==0):
            print(score)
            return
resolve()
