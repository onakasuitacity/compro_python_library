# https://atcoder.jp/contests/abc083/tasks/arc088_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

def bisection(l,r,f,left=True,discrete=True):
    eps=1 if discrete else 10**-12
    if((not left)^f(r)): return r if left else r+1
    elif(left^f(l)): return l-1 if left else l
    while(r-l>eps):
        h=(l+r)//2 if discrete else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if not discrete else l if left else r

def resolve():
    S=input()
    n=len(S)

    def check(k):
        if(n-k>=k): return True
        else: return len(set(S[n-k:k]))==1

    print(bisection(1,n,check))
resolve()
