# https://atcoder.jp/contests/abc082/tasks/arc087_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from itertools import groupby
def resolve():
    S=input()
    X=[]; Y=[]
    dir=0
    for key,iter in groupby(S):
        h=len(list(iter))
        if(key=='T'): dir^=(h&1)
        else:
            if(dir&1==0): X.append(h)
            else: Y.append(h)

    # 最初が移動のときだけは自由度が無いため例外処理
    tx,ty=map(int,input().split())
    if(S[0]=='F'):
        tx-=X[0]
        del X[0]

    # あとはx,y独立に移動できるので、tx、tyが到達可能かを判定
    M=8100*2
    dpx=[0]*M; dpx[0]=1
    dpy=[0]*M; dpy[0]=1

    for x in X:
        ndpx=[0]*M
        for i in range(M):
            if(dpx[i]==0): continue
            ndpx[(i+x)%M]=1
            ndpx[(i-x)%M]=1
        dpx=ndpx

    for y in Y:
        ndpy=[0]*M
        for i in range(M):
            if(dpy[i]==0): continue
            ndpy[(i+y)%M]=1
            ndpy[(i-y)%M]=1
        dpy=ndpy

    print("Yes" if(dpx[tx%M] and dpy[ty%M]) else "No")
resolve()
