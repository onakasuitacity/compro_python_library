# https://atcoder.jp/contests/abc133/tasks/abc133_f
# PyPyだとTLE
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class LCA(object):
    def __init__(self,E,root=0):
        self.__n=len(E)
        self.__E=E
        self.__logn=(self.__n-1).bit_length()
        self.__depth=[-1]*self.__n
        self.__dist=[-1]*self.__n
        self.__depth[root]=0
        self.__dist[root]=0
        self.__parents=[[-1]*self.__n for _ in range(self.__logn)]
        self.__dfs(root)
        self.__doubling()

    def __dfs(self,v):
        for u,c,d in self.__E[v]: # この問題用にライブラリを変形している
            if(self.__depth[u]!=-1): continue
            self.__parents[0][u]=v
            self.__depth[u]=self.__depth[v]+1
            self.__dist[u]=self.__dist[v]+d
            self.__dfs(u)

    def __doubling(self):
        for i in range(1,self.__logn):
            for v in range(self.__n):
                if(self.__parents[i-1][v]==-1): continue
                self.__parents[i][v]=self.__parents[i-1][self.__parents[i-1][v]]

    @property
    def depth(self):
        return self.__depth

    @property
    def dist(self):
        return self.__dist

    def get(self,u,v):
        dd=self.__depth[v]-self.__depth[u]
        if(dd<0): # vの方が深いようにする
            u,v=v,u
            dd*=-1
        for i in range(self.__logn):
            if(dd&(1<<i)): v=self.__parents[i][v]
        if(v==u): return v
        for i in range(self.__logn-1,-1,-1):
            pu,pv=self.__parents[i][u],self.__parents[i][v]
            if(pu!=pv): u,v=pu,pv
        return self.__parents[0][u]

def resolve():
    n,q=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b,c,d=map(int,input().split())
        a-=1; b-=1
        E[a].append((b,c,d))
        E[b].append((a,c,d))
    G=LCA(E)

    # Queryを先読みする
    Qs=[[] for _ in range(n)] #Q[v]: idx, color, mag, coef
    for i in range(q):
        x,y,u,v=map(int,input().split())
        u-=1; v-=1
        c=G.get(u,v)
        Qs[u].append((i,x,y,1))
        Qs[v].append((i,x,y,1))
        Qs[c].append((i,x,y,-2))

    # dfsでクエリに答えていく
    ans=[0]*q
    S=[[0,0] for _ in range(n)] # S[col]: total num, total len
    def dfs(v,p):
        # クエリに答える
        # 現在のlengthから、色のtotal lenを引き、青の個数*倍率(mug)を足したものが変更後の長さ
        for idx,col,mag,coef in Qs[v]:
            x=G.dist[v]
            x-=S[col][1]
            x+=mag*S[col][0]
            ans[idx]+=x*coef
        # 遷移
        for nv,col,d in E[v]:
            if(nv==p): continue
            S[col][0]+=1
            S[col][1]+=d
            dfs(nv,v)
            S[col][0]-=1
            S[col][1]-=d
    dfs(0,-1)
    print(*ans,sep="\n")
resolve()
