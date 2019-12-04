# https://atcoder.jp/contests/abc013/tasks/abc013_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

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
    n,h=map(int,input().split())
    a,b,c,d,e=map(int,input().split())

    ans=INF
    # k : 普通の食事を k 回行う
    for k in range(0,n+1):
        def check(x): # 質素な食事を x 日行ってOKか
            return h+b*k+d*x-e*(n-x-k)>0
        x=bisection(0,n-k,check,left=False)
        ans=min(ans,a*k+c*x)
    print(ans)
resolve()
