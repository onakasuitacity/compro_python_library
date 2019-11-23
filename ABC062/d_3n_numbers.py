# https://atcoder.jp/contests/abc062/tasks/arc074_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from heapq import heapify,heappop,heappush
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    P=[None]*(n+1); S=[None]*(n+1)

    # prefix
    Q=A[:n]
    P[0]=sum(Q)
    heapify(Q)
    for i in range(1,n+1):
        a=heappop(Q)
        b=A[n+i-1]
        P[i]=P[i-1]-a+max(a,b)
        heappush(Q,max(a,b))

    # suffix
    Q=[-a for a in A[2*n:]]
    S[-1]=sum(Q)
    heapify(Q)
    for i in range(n-1,-1,-1):
        a=heappop(Q)
        b=-A[n+i]
        S[i]=S[i+1]-a+max(a,b)
        heappush(Q,max(a,b))

    print(max(*(p+s for p,s in zip(P,S))))
resolve()
