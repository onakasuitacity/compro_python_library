# https://atcoder.jp/contests/arc024/tasks/arc024_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from collections import Counter
    l,r=map(int,input().split())
    L=Counter(map(int,input().split()))
    R=Counter(map(int,input().split()))
    ans=0
    for k,v in R.items():
        ans+=min(L[k],v)
    print(ans)
resolve()
