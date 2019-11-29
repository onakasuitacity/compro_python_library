# https://atcoder.jp/contests/abc047/tasks/arc063_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,t=map(int,input().split())
    A=list(map(int,input().split()))
    S=[None]*n
    S[-1]=A[-1]
    for i in range(n-2,-1,-1):
        S[i]=max(A[i],S[i+1])
    d=max(S[i+1]-A[i] for i in range(n-1))
    print(sum(1 for i in range(n-1) if(S[i+1]-A[i]==d)))
resolve()
