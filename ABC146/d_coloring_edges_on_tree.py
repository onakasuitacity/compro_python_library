# https://atcoder.jp/contests/abc146/tasks/abc146_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    idx={}
    for i in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)
        idx[(a,b)]=i

    ans=[None]*(n-1)
    k=max(len(E[v]) for v in range(n))

    # DFSで辺に色付け
    Q=[0]
    while(Q):
        v=Q.pop()
        if(v):
            p=min(E[v]) # 親はE[v]の最小値
            c=ans[idx[(p,v)]] # 親につながる色
        cnt=1
        for nv in E[v]:
            if(v==0):
                ans[idx[(v,nv)]]=cnt
                cnt+=1
                Q.append(nv)
            else:
                if(cnt==c): cnt+=1
                if(nv==p): continue
                ans[idx[(v,nv)]]=cnt
                cnt+=1
                Q.append(nv)

    print(k)
    for c in ans:
        print(c)

resolve()
