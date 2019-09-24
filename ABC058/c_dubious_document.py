# https://atcoder.jp/contests/abc058/tasks/arc071_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    from collections import Counter
    S=[Counter(input()) for _ in range(n)]
    ans=''
    for s in "abcdefghijklmnopqrstuvwxyz":
        ans+=s*min(c[s] for c in S)
    print(ans)
resolve()
