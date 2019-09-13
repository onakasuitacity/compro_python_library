#%% DFS + Euler Tour
# https://www.slideshare.net/yumainoue965/lca-and-rmq
# http://hos.ac/slides/20110504_graph.pdf

# const
INF=float("inf")

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

# parameter
root=0

# build
Tour=[]
Dist=[INF if i!=root else 0 for i in V]

# Euler Tour (recursive)
def DFS(parent,child):
    if parent is not None: Tour.append(parent)
    for v in E[child]:
        if Dist[v]==INF:
            Dist[v]=Dist[child]+1
            DFS(child,v)
    Tour.append(child)

DFS(None,root)
print(Dist)
print(Tour)
