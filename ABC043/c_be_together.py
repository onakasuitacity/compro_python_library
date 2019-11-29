# https://atcoder.jp/contests/abc043/tasks/arc059_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))

    ans=INF
    for x in range(-100,101):
        score=0
        for a in A:
            score+=(a-x)**2
        ans=min(ans,score)
    print(ans)
resolve()
