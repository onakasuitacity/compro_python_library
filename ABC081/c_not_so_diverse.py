# https://atcoder.jp/contests/abc081/tasks/arc086_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    from collections import Counter
    C=Counter(map(int,input().split()))
    l=len(C)
    if l<=k:
        print(0)
        return
    v=sorted(list(C.values()))
    print(sum(v[:l-k]))
resolve()
