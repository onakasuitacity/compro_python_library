# https://atcoder.jp/contests/arc021/tasks/arc021_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    B=[int(input()) for _ in range(n)]
    S=[0]*n
    for i in range(n-1):
        S[i+1]=S[i]^B[i]

    if(S[-1]!=B[-1]):
        print(-1)
    else:
        print(*S,sep='\n')
resolve()
