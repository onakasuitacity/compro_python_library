https://atcoder.jp/contests/abc142/tasks/abc142_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    H=list(map(int,input().split()))
    ans=0
    for h in H:
        ans+=(h>=k)
    print(ans)
resolve()
