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
    from bisect import bisect_left
    p=n
    i=bisect_left(A,p) # pに応じてiが定まる
    for k in range(1,n+1):
        while(S[i]+p*(m-i)<k*p): # p>=0 and は書かなくてもよい
            p-=1
            i=bisect_left(A,p)
        print(p)
resolve()

