# https://atcoder.jp/contests/pakencamp-2019-day4/tasks/pakencamp_2019_day4_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()

class LCA(object):
    def __init__(self,E,root=0):
        self.__n=len(E); self.__E=E; self.__logn=(self.__n-1).bit_length()
        self.__depth=[-1]*self.__n; self.__depth[root]=0
        self.__dist=[-1]*self.__n; self.__dist[root]=0
        self.__parents=[[-1]*self.__n for _ in range(self.__logn)]
        self.__dfs(root); self.__doubling()

    def __dfs(self,v):
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv,w in self.__E[v]:
                if(self.__depth[nv]!=-1): continue
                self.__parents[0][nv]=v
                self.__depth[nv]=self.__depth[v]+1
                self.__dist[nv]=self.__dist[v]+w
                Q.append(nv)

    def __doubling(self):
        for i in range(1,self.__logn):
            for v in range(self.__n):
                if(self.__parents[i-1][v]==-1): continue
                self.__parents[i][v]=self.__parents[i-1][self.__parents[i-1][v]]

    def kth_parent(self,k,v):
        return self.__parents[k][v]

    def depth(self,v):
        return self.__depth[v]

    def dist(self,v):
        return self.__dist[v]

    def get(self,u,v):
        dd=self.__depth[v]-self.__depth[u]
        if(dd<0): # vの方が深いようにする
            u,v=v,u
            dd*=-1
        for i in range(self.__logn):
            if((dd>>i)&1): v=self.__parents[i][v]
        if(v==u): return v
        for i in range(self.__logn-1,-1,-1):
            pu,pv=self.__parents[i][u],self.__parents[i][v]
            if(pu!=pv): u,v=pu,pv
        return self.__parents[0][u]

def resolve():
    n,K=map(int,input().split())
    logn=(n-1).bit_length()
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v,w=map(int,input().split())
        u-=1; v-=1
        E[u].append((v,w))
        E[v].append((u,w))
    lca=LCA(E)

    # 各 v に対して、1回の蘇生でどこまで登れるかを考える
    D=[None]*n
    for v in range(n):
        now=0
        w=v
        for k in range(logn-1,-1,-1):
            p=lca.kth_parent(k,w)
            if(p==-1): continue
            dd=lca.dist(w)-lca.dist(p)
            if(now+dd<K):
                now+=dd
                w=p
        D[v]=lca.kth_parent(0,w)

    # doubling により、2^k 回の蘇生でどこまで登れるかを考える
    dbl=[None]*logn
    dbl[0]=D
    for k in range(logn-1):
        D=[None]*n
        for v in range(n):
            D[v]=dbl[k][dbl[k][v]] if(dbl[k][v]!=-1) else -1
        dbl[k+1]=D

    # 各クエリを消化する
    for _ in range(int(input())):
        a,b=map(int,input().split())
        a-=1; b-=1
        ans=0

        c=lca.get(a,b)
        r=0
        for v in (a,b): # lca まで登れるところまで登る
            for k in range(logn-1,-1,-1):
                p=dbl[k][v]
                if(p!=-1 and lca.depth(c)<=lca.depth(p)):
                    ans+=1<<k # 2^k 回蘇生している
                    v=p
            r+=lca.dist(v)-lca.dist(c)

        ans+=r>=K # 残りは 0<=r<=2(K-1) で、K以上ならもう1回蘇生する必要あり
        print(ans)
resolve()
