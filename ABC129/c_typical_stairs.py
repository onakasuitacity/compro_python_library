# https://atcoder.jp/contests/abc129/tasks/abc129_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    fib=[0,1]
    a,b=0,1
    for _ in range(n):
        a,b=b,(a+b)%MOD
        fib.append(b)
    A=[-1]+[int(input()) for _ in range(m)]+[n+1]
    ans=1
    for i in range(m+1):
        ans*=fib[A[i+1]-A[i]-1]%MOD
    print(ans%MOD)

resolve()
