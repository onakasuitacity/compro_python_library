# https://atcoder.jp/contests/abc119/tasks/abc119_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,q=map(int,input().split())
    S=[-INF]+[int(input()) for _ in range(a)]+[INF]
    T=[-INF]+[int(input()) for _ in range(b)]+[INF]
    X=[int(input()) for _ in range(q)]
    from bisect import bisect
    for x in X:
        i=bisect(S,x)
        j=bisect(T,x)
        sleft=x-S[i-1]
        sright=S[i]-x
        tleft=x-T[j-1]
        tright=T[j]-x
        LL=max(sleft,tleft)
        RR=max(sright,tright)
        LR=sleft+tright+min(sleft,tright)
        RL=sright+tleft+min(sright,tleft)
        print(min(LL,RR,LR,RL))
resolve()
