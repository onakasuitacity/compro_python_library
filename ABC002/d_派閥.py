# https://atcoder.jp/contests/abc002/tasks/abc002_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    com=set()
    for _ in range(m):
        x,y=map(int,input().split())
        x,y=min(x,y)-1,max(x,y)-1
        com.add((x,y))
    ans=0
    from itertools import chain,combinations
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    for A in powerset(range(n)):
        B=set(combinations(A,2))
        if B<=com: ans=max(ans,len(A))
    print(ans)
resolve()
