# https://atcoder.jp/contests/abc104/tasks/abc104_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import ceil
    d,g=map(int,input().split())
    g//=100
    P=[0]*d
    C=[0]*d
    for i in range(d):
        p,c=map(int,input().split())
        c//=100
        P[i],C[i]=p,c

    def check(S):
        comp=[0]*d
        for i in range(d):
            comp[i]=S&1
            S>>=1
        score=0
        cnt=0
        for i in range(d):
            if(comp[i]):
                score+=(i+1)*P[i]+C[i]
                cnt+=P[i]

        # コンプした問題だけでクリアしていれば返す
        if(score>=g):
            return cnt

        # そうでなければ、解いてない問題のうち最大点数のものを何問解くか考える
        idx=-1
        for i in range(d-1,-1,-1):
            if(comp[i]==0):
                idx=i
                break

        if(idx==-1):
            return False

        k=ceil((g-score)/(idx+1))
        if(k<P[idx]):
            return cnt+k
        else:
            return False


    # completeする問題を全て試す
    ans=INF
    for S in range(2**d):
        score=check(S)
        if(score): ans=min(score,ans)
    print(ans)
resolve()
