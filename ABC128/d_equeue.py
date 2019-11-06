# https://atcoder.jp/contests/abc128/tasks/abc128_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    V=list(map(int,input().split()))

    from itertools import product
    import heapq
    score=0
    # l,r : 左、右から取り出す個数
    for l,r in product(range(0,k+1),repeat=2):
        if(l+r>k or l+r>n): continue
        A=[]
        for i in range(l):
            heapq.heappush(A,V[i])
        for i in range(n-r,n):
            heapq.heappush(A,V[i])
        for _ in range(k-l-r):
            if(A):
                a=heapq.heappop(A)
                if(a>0):
                    heapq.heappush(A,a)
        score=max(score,sum(A))
    print(score)
resolve()
