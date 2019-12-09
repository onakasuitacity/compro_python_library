# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    w,h=map(int,input().split())
    PQ=[None]*(w+h)
    for i in range(w):
        PQ[i]=(int(input()),0)
    for j in range(h):
        PQ[w+j]=(int(input()),1)
    PQ.sort()

    ans=0
    cnt=[h+1,w+1]
    for c,q in PQ:
        ans+=cnt[q]*c
        cnt[1-q]-=1
    print(ans)
resolve()
