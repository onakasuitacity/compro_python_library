# https://atcoder.jp/contests/abc127/tasks/abc127_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left as bisect
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    BC=[tuple(map(int,input().split())) for _ in range(m)]
    BC.sort(lambda x:-x[1])

    now=0
    ans=0
    for b,c in BC:
        i=bisect(A,c)
        if(i<=now): continue
        next=min(i,now+b)
        ans+=c*(next-now)
        now=next
    print(ans+sum(A[now:]))
resolve()
