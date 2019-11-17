# https://atcoder.jp/contests/abc145/tasks/abc145_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    C=[0]*n
    for i in range(n):
        x,y=map(int,input().split())
        C[i]=complex(x,y)

    S=sum(abs(C[i]-C[j]) for j in range(n) for i in range(n))
    print(S/n)
resolve()
