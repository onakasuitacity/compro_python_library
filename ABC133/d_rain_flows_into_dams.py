# https://atcoder.jp/contests/abc133/tasks/abc133_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    S=sum(A)
    oddS=sum(A[i] for i in range(1,n,2))
    ans=[0]*n
    ans[0]=S-2*oddS
    for i in range(n-1):
        ans[i+1]=2*A[i]-ans[i]
    print(*ans)
resolve()
