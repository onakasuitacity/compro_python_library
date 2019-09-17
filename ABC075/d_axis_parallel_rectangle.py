# https://atcoder.jp/contests/abc075/submissions/7579485
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    from itertools import product
    n,k=map(int,input().split())
    X=[0]*n
    Y=[0]*n
    XY=[0]*n
    for i in range(n):
        x,y=map(int,input().split())
        X[i]=x
        Y[i]=y
        XY[i]=(x,y)
    # 2-dim cumsum (pivot=(-inf,-inf))
    S=[[0]*n for _ in range(n)]
    X.sort(); Y.sort()
    for i,j in product(range(n),repeat=2):
        for x,y in XY:
            if x<=X[i] and y<=Y[j]: S[i][j]+=1
    # calculate
    ans=INF
    for i0,j0 in product(range(n),repeat=2):
        for i1,j1 in product(range(i0+1,n),range(j0+1,n)):
            count=S[i1][j1]
            if i0>0: count-=S[i0-1][j1]
            if j0>0: count-=S[i1][j0-1]
            if i0>0 and j0>0: count+=S[i0-1][j0-1]
            if count>=k:
                ans=min(ans,(X[i1]-X[i0])*(Y[j1]-Y[j0]))
    print(ans)
resolve()
