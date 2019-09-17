# https://atcoder.jp/contests/abc045/tasks/arc061_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    s=input()
    n=len(s)
    ans=0
    from itertools import product
    for A in product(range(2),repeat=n-1):
        k=s[0]
        for i in range(n-1):
            k+='+' if A[i] else ''
            k+=s[i+1]
        ans+=eval(k)
    print(ans)
resolve()
