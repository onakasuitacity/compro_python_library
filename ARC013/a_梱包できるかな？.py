# https://atcoder.jp/contests/arc013/tasks/arc013_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import permutations
    n,m,l=map(int,input().split())
    A=list(map(int,input().split()))
    B=permutations(A)
    ans=0
    for p,q,r in B:
        ans=max(ans,(n//p)*(m//q)*(l//r))
    print(ans)
resolve()
