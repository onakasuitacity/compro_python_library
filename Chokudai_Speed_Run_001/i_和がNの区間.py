# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_i
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from bisect import bisect_left as bisect
    n=int(input())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]

    cnt=0
    for i in range(n):
        j=bisect(S,S[i]+n)
        if(j<=n):
            cnt+=S[j]==S[i]+n
    print(cnt)
resolve()
