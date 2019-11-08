# https://atcoder.jp/contests/abc131/tasks/abc131_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,l=map(int,input().split())
    A=[l+i for i in range(n)]
    S=sum(A)
    a=INF
    for i in range(n):
        if(abs(a)>abs(A[i])):
            a=A[i]
    print(S-a)
resolve()
