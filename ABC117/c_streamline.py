# https://atcoder.jp/contests/abc117/tasks/abc117_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    if n>=m:
        print(0)
        return
    X=list(map(int,input().split()))
    X.sort()
    D=[0]*(m-1)
    for i in range(m-1):
        D[i]=(i,X[i+1]-X[i])
    from operator import itemgetter
    D.sort(key=itemgetter(1),reverse=1)
    ans=0
    ppos=0
    for i in range(n-1):
        pos=D[i][0]
        ans+=X[pos]-X[ppos]
        ppos=pos+1
    print(ans+X[-1]-X[ppos])
resolve()
