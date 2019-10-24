# https://atcoder.jp/contests/abc137/tasks/abc137_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    p=int(input())
    r=[0]*(p+1)
    r[1]=-1; r[p]=1
    ans=[0]*p
    for i,a in enumerate(map(int,input().split())):
        if(not a): continue
        u=[0]*(p+1) # u(x)=r(x)/(x-i)
        for k in range(p-1,-1,-1):
            u[k]=(r[k+1]+i*u[k+1])%p
            ans[k]-=u[k]
            ans[k]%=p
    print(*ans)
resolve()
