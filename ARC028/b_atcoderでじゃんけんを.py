# https://atcoder.jp/contests/arc048/tasks/arc048_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    C=[0]*100001
    RH=[None]*n
    DRH=[[0]*3 for _ in range(100001)]
    for i in range(n):
        r,h=map(int,input().split())
        h-=1
        C[r]+=1
        RH[i]=(r,h)
        DRH[r][h]+=1
    for i in range(100000):
        C[i+1]+=C[i]

    for r,h in RH:
        win=C[r-1]+DRH[r][(h+1)%3]
        draw=DRH[r][h]
        lose=n-win-draw
        print(win,lose,draw-1)
resolve()
