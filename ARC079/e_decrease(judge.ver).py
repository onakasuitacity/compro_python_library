# https://atcoder.jp/contests/arc079/tasks/arc079_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    s=sum(A)

    while(max(A)>=n):
        k=sum(a//n for a in A)
        for i in range(n):
            A[i]+=(k-A[i]//n)-n*(A[i]//n)

    print(s-sum(A))
resolve()
