# https://atcoder.jp/contests/abc021/tasks/abc021_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def modinv(a,m):
    b,u,v=m,1,0
    while(b):
        t=a//b
        a-=t*b; a,b=b,a
        u-=t*v; u,v=v,u
    u%=m
    if u<0: u+=m
    return u
def resolve():
    from math import factorial
    n,k=[int(input()) for _ in range(2)]
    if n==1:
        print(1)
        return
    m=max(n,k)
    factinv=[0]*m
    factinv[0]=modinv(factorial(m),MOD)
    for i in range(1,m):
        factinv[i]=factinv[i-1]*(m-i+1)%MOD
    factinv.reverse()
    print(factorial(n+k-1)%MOD*factinv[k-1]*factinv[n-2]%MOD)
resolve()
