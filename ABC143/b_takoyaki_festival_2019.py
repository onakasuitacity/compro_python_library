# https://atcoder.jp/contests/abc143/tasks/abc143_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    D=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ans+=D[i]*D[j]
    print(ans)
resolve()
