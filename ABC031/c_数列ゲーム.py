# https://atcoder.jp/contests/abc031/tasks/abc031_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))

    ans=-INF
    for i in range(n):
        takahashi=INF
        aoki=-INF
        for j in range(n):
            if(i==j): continue
            T=A[min(i,j):max(i,j)+1]
            s=sum(T)
            t=sum(a for k,a in enumerate(T) if(k&1))
            if(t>aoki):
                aoki=t
                takahashi=s-t
        ans=max(ans,takahashi)
    print(ans)
resolve()
