# https://atcoder.jp/contests/abc107/tasks/arc101_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,k=map(int,input().split())
    X=tuple(map(int,input().split()))
    ans=INF
    for i in range(n-k+1):
        a,b=X[i],X[i+k-1]
        if a<0<b:
            ans=min(ans,b-a+min(-a,b))
        else:
            ans=min(ans,max(abs(a),abs(b)))
    print(ans)
resolve()
