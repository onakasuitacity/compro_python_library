# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    ans=1
    C=[0]*(n+1)
    C[0]=3
    for a in A:
        ans*=C[a]
        ans%=MOD
        C[a]-=1
        C[a+1]+=1
    print(ans)
resolve()
