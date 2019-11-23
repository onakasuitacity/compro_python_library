# https://atcoder.jp/contests/abc032/tasks/abc032_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from bisect import bisect
def resolve():
    n,W=map(int,input().split())
    VW=[tuple(map(int,input().split())) for _ in range(n)]

    # n <= 30 -> 半分に分けてmerge
    if(n<=30):
        ans=0
        A=VW[:n//2]; B=VW[n//2:]
        P=[None]*(2**(n//2))
        Q=[None]*(2**(n-n//2))
        # それぞれ全列挙 (O(n2^(n/2)))
        for S in range(2**(n//2)):
            v,w=0,0
            for i in range(n//2):
                if(S&(1<<i)):
                    v+=VW[i][0]
                    w+=VW[i][1]
            P[S]=(w,v)
        for S in range(2**(n-n//2)):
            v,w=0,0
            for i in range(n-n//2):
                if(S&(1<<i)):
                    v+=VW[n//2+i][0]
                    w+=VW[n//2+i][1]
            Q[S]=(w,v)
        # 不要なものを削除してPの全順序部分集合を抽出
        P.sort(lambda x:(x[0],-x[1]))
        R=[P[0]]
        for i in range(2**(n//2)-1):
            if(P[i][1]<P[i+1][1]):
                R.append(P[i+1])
        # Qの各元に対して、Rの最適なものを二分探索 (O(n2^(n/2)))
        for w,v in Q:
            if(w>W): continue
            i=bisect(R,(W-w,INF))
            ans=max(ans,v+R[i-1][1])
        print(ans)
        return

    # VMAX <= 2*10^5 -> knapsack 2
    VMAX=sum(v for v,w in VW)
    if(VMAX<=2*(10**5)):
        dp=[INF]*(VMAX+1)
        dp[0]=0
        for i in range(n):
            v,w=VW[i]
            ndp=dp[:]
            for v0 in range(VMAX):
                if(v+v0<=VMAX):
                    ndp[v+v0]=min(ndp[v+v0],dp[v0]+w)
            dp=ndp
        for i in range(VMAX,-1,-1):
            if(dp[i]<=W):
                print(i)
                return

    # WMAX <= 2*10^5 -> knapsack 1
    WMAX=sum(w for v,w in VW)
    if(WMAX<=2*(10**5)):
        dp=[-INF]*(WMAX+1)
        dp[0]=0
        for i in range(n):
            ndp=dp[:]
            v,w=VW[i]
            for w0 in range(WMAX+1):
                if(w+w0<=WMAX):
                    ndp[w+w0]=max(ndp[w+w0],dp[w0]+v)
            dp=ndp
        print(max(dp[:W+1]))
        return
resolve()
