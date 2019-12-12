# https://atcoder.jp/contests/agc036/tasks/agc036_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    idx=[[] for _ in range(max(A)+1)]
    for i,a in enumerate(A):
        idx[a].append(i)

    # いくつ先に移動するかを求める
    next=[None]*n
    for I in idx:
        if(not I): continue
        s=len(I)
        I.append(I[0]+n)
        for i in range(s):
            next[I[i]]=I[i+1]-I[i]+1

    # doubling
    M=10**18 # n*k より大きな数で抑えておく
    nexts=[next]
    for _ in range(60):
        next=nexts[-1]
        nnext=[min(M,next[i]+next[(i+next[i])%n]) for i in range(n)]
        nexts.append(nnext)

    now=0
    for next in nexts[::-1]:
        if(now+next[now%n]<=n*k):
            now+=next[now%n]
    if(now==n*k):
        return

    # A[now%n:] に対してシミュレーションする
    ans=[]
    have=[0]*(max(A)+1)
    for a in A[now%n:]:
        if(not have[a]):
            ans.append(a)
            have[a]=1
        else:
            while(1):
                x=ans.pop()
                have[x]=0
                if(x==a): break

    print(*ans)
resolve()
