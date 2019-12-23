# https://atcoder.jp/contests/abc148/tasks/abc148_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))

    now=0
    for a in A:
        if(a==now+1):
            now+=1

    if(now==0):
        print(-1)
    else:
        print(n-now)
resolve()
