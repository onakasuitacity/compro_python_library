# https://atcoder.jp/contests/abc027/tasks/abc027_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    if(sum(A)%n):
        print(-1)
        return
    k=sum(A)//n
    for i in range(n-1):
        A[i+1]+=A[i]

    ans=n
    for i in range(n):
        ans-=A[i]==k*(i+1)
    print(ans)
resolve()
