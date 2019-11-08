# https://atcoder.jp/contests/abc124/tasks/abc124_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    n,k=map(int,input().split())
    s=input()
    G=groupby(s)
    A=[]
    cnt=0
    if(s[0]=='0'): A.append(0)
    for key,iter in G:
        cnt+=key=='0'
        A.append(len(list(iter)))
    if(s[-1]=='0'): A.append(0)
    if(cnt<=k):
        print(n)
        return

    n=len(A)
    now=sum(A[:2*k+1])
    score=now
    for i in range(2*k+2,n,2):
        now+=A[i]+A[i-1]-A[i-2*k-2]-A[i-2*k-1]
        score=max(score,now)
    print(score)
resolve()
