# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    s=sum(A)
    for i in range(n-1):
        A[i+1]+=A[i]
    ans=INF
    for i in range(n-1):
        ans=min(ans,abs(A[i]-(s-A[i])))
    print(ans)
resolve()
