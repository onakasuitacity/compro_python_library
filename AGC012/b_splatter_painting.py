# https://atcoder.jp/contests/agc012/tasks/agc012_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    q=int(input())
    VDC=[None]*q
    for i in range(q):
        v,d,c=map(int,input().split())
        v-=1
        VDC[i]=(v,d,c)
    VDC.reverse()

    dp=[[0]*11 for _ in range(n)]
    ans=[0]*n

    for v,d,c in VDC:
        Q=deque([(v,d)])
        dp[v][d]=1
        while(Q):
            v,d=Q.popleft()
            if(d>0):
                if(not dp[v][d-1]):
                    dp[v][d-1]=1
                    Q.append((v,d-1))
                for nv in E[v]:
                    if(dp[nv][d-1]): continue
                    dp[nv][d-1]=1
                    Q.append((nv,d-1))
            if(ans[v]==0):
                ans[v]=c

    print(*ans,sep='\n')
resolve()
