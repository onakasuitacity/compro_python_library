# https://atcoder.jp/contests/abc074/tasks/abc074_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=int(input()),int(input())
    X=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if X[i]<=0: ans+=abs(X[i])
        elif X[i]>=k: ans+=X[i]-k
        else: ans+=min(X[i],k-X[i])
    print(ans*2)
resolve()
