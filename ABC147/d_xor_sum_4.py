# https://atcoder.jp/contests/abc147/tasks/abc147_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=(n-1)*sum(A)
    ans%=MOD

    for d in range(60,-1,-1):
        cnt=sum((a>>d)&1 for a in A)
        k=cnt*(cnt-1)
        ans-=k<<d
        ans%=MOD
    print(ans)
resolve()
