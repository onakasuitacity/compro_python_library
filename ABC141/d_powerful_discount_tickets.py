# https://atcoder.jp/contests/abc141/tasks/abc141_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
import heapq
input=sys.stdin.readline
def resolve():
    n,m=map(int,input().split())
    A=list(map(lambda x:-(int(x)),input().split()))
    heapq.heapify(A)
    for _ in range(m):
        a=heapq.heappop(A)
        a=-a
        a=a>>1
        heapq.heappush(A,-a)
    print(-sum(A))
resolve()
