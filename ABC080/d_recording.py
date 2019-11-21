# https://atcoder.jp/contests/abc080/tasks/abc080_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,c=map(int,input().split())
    STC=[tuple(map(int,input().split())) for _ in range(n)]
    STC.sort(lambda x:(x[2],x[0],x[1]))

    # 同じチャンネルで連続するものは結合しておく
    for i in range(n-1):
        s0,t0,c0=STC[i]
        s1,t1,c1=STC[i+1]
        if(c0!=c1): continue
        if(t0==s1):
            STC[i]=(None,None,None)
            STC[i+1]=(s0,t1,c0)
    # 残りについて、[s-1,t)のimosを行う
    M=100000
    imos=[0]*(M+1)
    for s,t,c in STC:
        if(s is None): continue
        imos[s-1]+=1
        imos[t]-=1
    for i in range(M):
        imos[i+1]+=imos[i]
    print(max(imos))
resolve()
