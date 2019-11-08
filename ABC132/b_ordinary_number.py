# https://atcoder.jp/contests/abc132/tasks/abc132_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=0
    for i in range(1,n-1):
        ans+=(A[i-1]<A[i]<A[i+1]) or (A[i-1]>A[i]>A[i+1])
    print(ans)
resolve()
