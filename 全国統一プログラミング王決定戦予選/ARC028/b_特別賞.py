# https://atcoder.jp/contests/arc028/tasks/arc028_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from heapq import heappop,heappush,heapify
def resolve():
    n,k=map(int,input().split())
    XI=[(-x,i) for i,x in enumerate(map(int,input().split()),1)]

    Q=XI[:k]
    heapify(Q)
    print(Q[0][1])
    for x,i in XI[k:]:
        if(x>Q[0][0]):
            heappop(Q)
            heappush(Q,(x,i))
        print(Q[0][1])
resolve()
