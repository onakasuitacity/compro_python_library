# https://atcoder.jp/contests/abc010/tasks/abc010_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

from collections import deque
class Dinic(object):
    def __init__(self,n):
        self.__n=n
        self.__E=[[] for _ in range(n)]
        self.__level=None
        self.__iter=None

    def add_link(self,u,v,w):
        self.__E[u].append([v,w,len(self.__E[v])])
        self.__E[v].append([u,0,len(self.__E[u])-1])

    def __bfs(self,s):
        level=[-1]*self.__n
        level[s]=0
        Q=deque([s])
        while(Q):
            v=Q.popleft()
            for nv,w,rev in self.__E[v]:
                if(w>0 and level[nv]<0):
                    level[nv]=level[v]+1
                    Q.append(nv)
        self.__level=level

    def __dfs(self,v,t,flow):
        if(v==t): return flow
        for i in range(self.__iter[v],len(self.__E[v])):
            self.__iter[v]=i
            nv,w,rev=self.__E[v][i]
            if(w==0 or self.__level[v]>=self.__level[nv]): continue
            d=self.__dfs(nv,t,min(flow,w))
            if(d==0): continue
            self.__E[v][i][1]-=d
            self.__E[nv][rev][1]+=d
            return d
        return 0

    def flow(self,s,t):
        res=0
        while(True):
            self.__bfs(s)
            if(self.__level[t]<0): return res
            self.__iter=[0]*self.__n
            cur=self.__dfs(s,t,INF)
            while(cur):
                res+=cur
                cur=self.__dfs(s,t,INF)

def resolve():
    n,g,e=map(int,input().split())
    mf=Dinic(n+1)
    for p in map(int,input().split()):
        mf.add_link(p,n,1)
        mf.add_link(n,p,1)
    for _ in range(e):
        a,b=map(int,input().split())
        mf.add_link(a,b,1)
        mf.add_link(b,a,1)
    print(mf.flow(0,n))
resolve()
