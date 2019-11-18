# https://atcoder.jp/contests/abc095/tasks/arc096_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,c=map(int,input().split())
    X=[0]*n; V=[0]*n
    for i in range(n):
        X[i],V[i]=map(int,input().split())

    revX=[c-x for x in X]
    revV=V[:]

    for i in range(n-1):
        V[i+1]+=V[i]
    for i in range(n):
        V[i]-=X[i]

    maxV=V[:]
    for i in range(n-1):
        maxV[i+1]=max(maxV[i+1],maxV[i])


    for i in range(n-1,0,-1):
        revV[i-1]+=revV[i]
    for i in range(n-1,-1,-1):
        revV[i]-=revX[i]

    maxrevV=revV[:]
    for i in range(n-1,0,-1):
        maxrevV[i-1]=max(maxrevV[i-1],maxrevV[i])

    # 片方向だけ使った場合の最大を取っておく
    ans=max(max(maxV),max(maxrevV),0)

    # forward に i, backwardに最大 i+1 まで行く時の場合を試す
    for i in range(n-1):
        ans=max(ans,V[i]+maxrevV[i+1]-X[i])

    # backward に i, forwardに最大 i-1 まで行く時の場合を試す
    for i in range(1,n):
        ans=max(ans,revV[i]+maxV[i-1]-revX[i])

    print(ans)
resolve()
