# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    ans=0
    for _ in range(n):
        a,b=map(int,input().split())
        ans+=min(a//2,b)
    print(ans)
resolve()
