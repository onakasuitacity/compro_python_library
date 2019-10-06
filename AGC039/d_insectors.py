# https://atcoder.jp/contests/agc039/tasks/agc039_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,l=map(int,input().split())
    T=[int(input()) for _ in range(n)]
    import math,cmath
    pi=math.acos(-1)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ans+=cmath.rect(1,(T[i]+T[j])*pi/l)*(n-(j-i+1))
            ans+=-cmath.rect(1,(T[i]+T[j])*pi/l)*(j-i-1)
    ans/=n*(n-1)*(n-2)/6
    print(ans.real,ans.imag)
resolve()
