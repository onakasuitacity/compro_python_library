# https://atcoder.jp/contests/abc018/tasks/abc018_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m,p,q,r=map(int,input().split())
    happy={i:[] for i in range(n)}
    for _ in range(r):
        x,y,z=map(int,input().split())
        happy[x-1].append((y-1,z))
    from itertools import combinations
    ans=0
    for P in combinations(range(n),p):
        score=[0]*m
        for x in P:
            for y,z in happy[x]:
                score[y]+=z
        score.sort(reverse=1)
        ans=max(ans,sum(score[:q]))
    print(ans)
resolve()
