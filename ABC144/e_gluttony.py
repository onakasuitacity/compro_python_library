# https://atcoder.jp/contests/abc144/tasks/abc144_e
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
    n,k=map(int,input().split())
    A=sorted(map(int,input().split()))
    F=sorted(map(int,input().split()),reverse=1)
    def check(x):
        res=0
        for a,f in zip(A,F):
            if(a*f)<=x: continue
            res+=a-int(x/f)
        return res<=k
    print(bisection(0,10**12,check,left=False))
resolve()
