# https://atcoder.jp/contests/agc004/tasks/agc004_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    ans=sum(A)

    now=A[:]
    for i in range(1,n):
        now=[min(now[j],A[(i+j)%n]) for j in range(n)]
        ans=min(ans,sum(now)+i*x)

    print(ans)
resolve()
