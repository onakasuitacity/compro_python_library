# https://atcoder.jp/contests/abc148/tasks/abc148_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S,T=input().split()
    ans=[None]*(2*n)

    for i in range(n):
        ans[2*i]=S[i]
        ans[2*i+1]=T[i]

    print(''.join(ans))
resolve()
