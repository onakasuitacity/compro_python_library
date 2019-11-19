# https://atcoder.jp/contests/abc091/tasks/arc092_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

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
        flow=0
        while(True):
            self.__bfs(s)
            if(self.__level[t]<0): return flow
            self.__iter=[0]*self.__n
            current_flow=self.__dfs(s,t,INF)
            while(current_flow):
                flow+=current_flow
                current_flow=self.__dfs(s,t,INF)

def resolve():
    n=int(input())
    AB=[tuple(map(int,input().split())) for _ in range(n)]
    CD=[tuple(map(int,input().split())) for _ in range(n)]

    # bipartite の maximum matching で解く
    mf=Dinic(2*n+2)
    for i in range(n):
        mf.add_link(0,i+1,1)
        mf.add_link(n+i+1,2*n+1,1)
    for i in range(n):
        a,b=AB[i]
        for j in range(n):
            c,d=CD[j]
            if(a<c and b<d):
                mf.add_link(i+1,n+j+1,1)

    print(mf.flow(0,2*n+1))
resolve()
