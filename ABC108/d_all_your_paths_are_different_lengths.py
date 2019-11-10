# https://atcoder.jp/contests/abc108/tasks/arc102_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def iterate(L,n,m,edges,mode):
    # L -> L+1
    if(mode&1 or L==1):
        edges+=[(1,n,L)]
        return L+1,n,m+1,edges
    # L -> 2*L
    else:
        edges=[(u,v,2*w) for u,v,w in edges]
        edges+=[(n,n+1,0),(n,n+1,1)]
        return 2*L,n+1,m+2,edges
        
def resolve():
    L=int(input())
    res=[L%2]
    while(L!=1):
        if(L&1): L-=1
        else: L//=2
        res.append(L%2)
    res.reverse()

    # initialize
    L=1
    n=2
    m=1
    edges=[(1,2,0)]

    # iterate
    for mode in res[1:]:
        L,n,m,edges=iterate(L,n,m,edges,mode)

    # output
    print(n,m)
    for e in edges:
        print(*e)
resolve()
