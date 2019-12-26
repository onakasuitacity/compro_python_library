# https://atcoder.jp/contests/agc020/tasks/agc020_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    s=sum(A)

    dp=1
    for a in A:
        dp|=(dp<<a)

    for i in range((s+1)//2,s+1):
        if((dp>>i)&1):
            print(i)
            return
resolve()
