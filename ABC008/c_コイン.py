# https://atcoder.jp/contests/abc008/tasks/abc008_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    C=[int(input()) for _ in range(n)]
    fact=list(range(n+1))
    fact[0]=1
    for i in range(n):
        fact[i+1]*=fact[i]
    D=[0]*n
    for i in range(n):
        for j in range(n):
            if(i==j): continue
            D[i]+=(C[i]%C[j]==0)

    def comb(n,k):
        if(k<0 or n<k): return 0
        return fact[n]//(fact[k]*fact[n-k])

    ans=0
    for k in D:
        score=0
        for i in range(1,n+1):
            for j in range(0,k+1,2):
                score+=comb(i-1,j)*comb(n-i,k-j)
        ans+=score/(n*comb(n-1,k))
    print(ans)
resolve()
