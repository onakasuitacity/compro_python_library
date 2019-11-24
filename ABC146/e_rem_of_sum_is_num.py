# https://atcoder.jp/contests/abc146/tasks/abc146_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import defaultdict
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]

    for i in range(n+1):
        S[i]-=i
        S[i]%=k

    C=defaultdict(list)
    for i in range(n+1):
        C[S[i]].append(i)

    ans=0
    C=list(C.values())
    for d in range(len(C)):
        n=len(C[d])
        if(n<=1): continue
        r=0
        for l in range(n):
            while(r+1<n and C[d][r+1]-C[d][l]<k):
                r+=1
            ans+=r-l
            if(r==l): r+=1
    print(ans)
resolve()
