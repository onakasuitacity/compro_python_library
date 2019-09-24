# https://atcoder.jp/contests/abc057/tasks/abc057_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    V=[tuple(map(int,input().split())) for _ in range(n)]
    C=[tuple(map(int,input().split())) for _ in range(m)]
    ans=[0]*n
    for i in range(n):
        dist=INF
        ind=0
        for j in range(m):
            d=abs(V[i][0]-C[j][0])+abs(V[i][1]-C[j][1])
            if d<dist:
                ind=j
                dist=d
        print(ind+1)
resolve()
