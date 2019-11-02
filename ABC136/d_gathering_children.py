# https://atcoder.jp/contests/abc136/tasks/abc136_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import groupby
    s=input()
    n=len(s)
    G=groupby(s)
    A=[]
    for i,g in enumerate(G):
        key,iter=g
        if(i%2==0): a=len(list(iter))
        else: A.append((a,len(list(iter))))
    ans=[0]*n
    idx=-1
    for x,y in A:
        idx+=x
        ans[idx]=x-x//2+y//2
        ans[idx+1]=x//2+y-y//2
        idx+=y
    print(*ans)
resolve()
