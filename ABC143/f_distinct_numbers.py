# https://atcoder.jp/contests/abc143/tasks/abc143_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def bisection(l,r,f,discrete=True,left=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return h if not discrete else l if left else r

def resolve():
    from collections import Counter
    from bisect import bisect_left
    n=int(input())
    A=Counter(map(int,input().split()))
    A=list(A.values())
    A.sort()
    m=len(A)
    S=[0]*(m+1)# cumulative distribution
    for i in range(m):
        S[i+1]=S[i]+A[i]
    for k in range(1,n+1):
        def check(p):
            i=bisect_left(A,p)
            return S[i]+(m-i)*p>=k*p
        print(bisection(0,n//k+1,check))
resolve()
