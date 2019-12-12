# https://atcoder.jp/contests/agc007/tasks/agc007_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    M=20000
    A=[M*i for i in range(1,n+1)]
    B=[M*(n-i+1) for i in range(1,n+1)]
    perm=list(map(lambda x:int(x)-1,input().split()))
    for i in range(n):
        A[perm[i]]+=i

    print(*A)
    print(*B)
resolve()
