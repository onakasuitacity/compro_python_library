# https://atcoder.jp/contests/abc143/tasks/abc143_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left
    n=int(input())
    L=list(map(int,input().split()))
    L.sort()
    ans=0
    for i in range(1,n):
        for j in range(i+1,n):
            k=bisect_left(L,L[j]-L[i]+1)
            ans+=max(0,i-k)
    print(ans)
resolve()
