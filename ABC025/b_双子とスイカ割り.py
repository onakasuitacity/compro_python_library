# https://atcoder.jp/contests/abc025/tasks/abc025_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    ans=0
    for _ in range(n):
        s,d=input().split()
        ans+=min(max(a,int(d)),b)*(1 if s=="East" else -1)
    if ans>0:
        print("East",ans)
    elif ans<0:
        print("West",-ans)
    else:
        print(0)
resolve()
