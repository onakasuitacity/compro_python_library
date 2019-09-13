#%% LCA(Lowest Common Ancestor) & doubling
# https://tjkendev.github.io/procon-library/python/graph/lca-doubling.html

class LCA(object):
    def __init__(self,edges,root): # both adjacence matrix and adjacence list are acceptable as edges
        self.edges=edges
        self.root=root
        self.n=len(edges) # n=|V|
        self.logn=(self.n-1).bit_length() # logn = ceil(log2(n))
        # initialization
        self.depth=[float("inf") if i!=root else 0 for i in range(self.n)]
        self.parent=[[-1]*self.logn for _ in range(self.n)] # parent[u][i]=v : uの2^i世代上がv(なければ-1)
        # construct
        self.dfs(root)
        self.doubling()

    def dfs(self,u):
        for v in E[u]:
            if self.depth[v]==float("inf"): # 訪れていない＝深さがINF(rootから連結な部分しか探索しない)
                self.depth[v]=self.depth[u]+1
                self.parent[v][0]=u
                self.dfs(v)

    def doubling(self):
        for i in range(1,self.logn):
            for v in range(self.n):
                if self.parent[v][i-1]!=-1: # 半分遡った時点で親が存在しなければ-1のままにしておく。-1が返るとlistの末尾の値の取得になってしまう
                    self.parent[v][i]=self.parent[self.parent[v][i-1]][i-1]
    
    def get(self,u,v): # uとvとのLCAを返す
        dd=self.depth[v]-self.depth[u]
        if dd<0: # vの方が深いようにする
            u,v=v,u
            dd=-dd

        for i in range(self.logn): # dd分だけvを遡らせる
            if dd&1: # 各bitで判定
                v=self.parent[v][i]
            dd>>=1

        if u==v: return u # 高さ揃えた時点で一致してたら終わり

        for i in range(self.logn-1,-1,-1): # そうでなければ上から二分探索
            pu,pv=self.parent[u][i],self.parent[v][i]
            if pu!=pv:
                u,v=pu,pv
        return self.parent[u][0]

    def depth(self,v):
        return self.depth[v]
                
#%%
# given data
N=6
V=list(range(N))
E=[{1,2},{0},{0,3,4,5},{2},{3},{4}]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

a=LCA(E,0)
a.get(3,4) # 2
