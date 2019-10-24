# https://atcoder.jp/contests/abc137/tasks/abc137_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    # preparation
    p=int(input())
    invfact=[0]*p
    invfact[p-1]=p-1 # Wilson's theorem
    for i in range(2,p):
        invfact[p-i]=invfact[p-i+1]*(p-i+1)%p

    # initialize
    A=list(map(int,input().split()))
    ans=[0]*p
    ans[0]=A[0]
    r=[0]*(p+1) # for use of r[-1]=0
    r[0]=1

    # iterate
    for k in range(1,p):
        newr=[0]*(p+1) # newr(x)=(x-(k-1))r(x)
        v=0 # v=f[k-1](k)
        power=1
        for i in range(p):
            v+=ans[i]*power%p
            power*=k
            power%=p
            newr[i]=(r[i-1]-(k-1)*r[i])%p
        r=newr
        for i in range(p):
            ans[i]+=(A[k]-v)*invfact[k]*r[i]
            ans[i]%=p
    print(*ans)
resolve()
