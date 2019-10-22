# https://atcoder.jp/contests/abc143/tasks/abc143_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from collections import Counter
    n=int(input())
    A=list(Counter(map(int,input().split())).values())
    A.sort()
    m=len(A)
    S=[0]*(m+1) # cumulative distribution
    for i in range(m): S[i+1]=S[i]+A[i]
    # output
    p=n
    from bisect import bisect_left
    for k in range(1,n+1):
        while(1):
            # pに対して先にi_pを求めておく
            i=bisect_left(A,p)
            if(S[i]+p*(m-i)>=k*p): break
            p-=1 # pの条件が真になるまで減らし続ける
        print(p)
resolve()
