# https://yukicoder.me/problems/no/900
class SegmentTree(object):
    def __init__(self,A,dot,e,comp,id,act):
        """
        A: array of monoid (M,dot,e)
        comp: composite function of Hom(M), comp(f,g)=gf
        id: identity map of M
        act: action on (Hom(M),M), act(f,a)=f(a)
        """
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__comp=comp
        self.__id=id
        self.__act=act
        self.__node=[e]*(2*n)
        self.__lazy=[id]*(2*n)
        for i in range(len(A)):
            self.__node[i+n]=A[i]
        for i in range(n-1,0,-1):
            self.__node[i]=self.__dot(self.__node[2*i],self.__node[2*i+1])

    def __propagate(self,i):
        if(self.__lazy[i]==self.__id): return
        node=self.__node
        lazy=self.__lazy
        if(i<self.__n): # propagate to children
            lazy[2*i]=self.__comp(lazy[2*i],lazy[i])
            lazy[2*i+1]=self.__comp(lazy[2*i+1],lazy[i])
        node[i]=self.__act(lazy[i],node[i]) # action
        lazy[i]=self.__id

    def __ancestors_propagate(self,i):
        if(i==1): return
        i//=2
        self.__ancestors_propagate(i)
        self.__propagate(i)

    def __update_ancestors(self,i):
        while(i!=1):
            self.__propagate(i+1-2*(i%2)) # propagate the sibling of i
            i//=2
            self.__node[i]=self.__dot(self.__node[2*i],self.__node[2*i+1])

    def update(self,i,c):
        i+=self.__n
        self.__ancestors_propagate(i)
        self.__propagate(i)
        self.__node[i]=c
        self.__update_ancestors(i)

    def add(self,l,r,f):
        range,low=[],[0]*2
        l+=self.__n; r+=self.__n
        while(l<r):
            if(l%2==1):
                if(low[0]==0): low[0]=l
                range.append(l)
                l+=1
            l//=2
            if(r%2==1):
                r-=1
                range.append(r)
                if(low[1]==0): low[1]=r
            r//=2
        for i in low:
            if(i): self.__ancestors_propagate(i)
        for i in range: self.__lazy[i]=self.__comp(self.__lazy[i],f)
        for i in low:
            if(i):
                self.__propagate(i)
                self.__update_ancestors(i)

    def sum(self,l,r):
        range,low=[],[0]*2
        vl,vr=self.__e,self.__e
        l+=self.__n; r+=self.__n
        while(l<r):
            if(l%2==1):
                if(low[0]==0):
                    self.__ancestors_propagate(l)
                    low[0]=1
                self.__propagate(l)
                vl=self.__dot(vl,self.__node[l])
                l+=1
            l//=2
            if(r%2==1):
                r-=1
                if(low[1]==0):
                    self.__ancestors_propagate(r)
                    low[1]=1
                self.__propagate(r)
                vr=self.__dot(self.__node[r],vr)
            r//=2
        return self.__dot(vl,vr)

class EulerTour(object):
    def __init__(self,E,root=0):
        """
        E: adjacency list (with weight)
        root: int
        """
        n=len(E)
        self.__V=list(range(n))
        self.__E=E 
        self.__begin=[0]*n
        self.__end=[0]*n
        self.__tour=[(0,0)]*(2*n)
        self.__k=0
        self.__dfs(root,-1)
        del self.__k

    def __dfs(self,v,p):
        self.__begin[v]=self.__k
        self.__k+=1
        for u in self.__E[v]:
            if u[0]==p: continue
            self.__tour[self.__k]=(u[1],1)
            self.__dfs(u[0],v)
            self.__tour[self.__k]=(-u[1],-1)
            self.__k+=1
        self.__end[v]=self.__k

    @property
    def begin(self):
        return self.__begin

    @property
    def end(self):
        return self.__end

    @property
    def tour(self):
        return self.__tour

import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    # input
    n=int(input())
    E=[[] for _ in range(n)] # adjecency list
    for _ in range(n-1):
        u,v,w=map(int,input().split())
        E[u].append((v,w))
    # build
    tour=EulerTour(E)
    dot=lambda a,b:(a[0]+b[0],a[1]+b[1])
    e=(0,0)
    comp=lambda f,g:g+f
    id=0
    act=lambda f,a:(a[0]+f*a[1],a[1])
    tree=SegmentTree(tour.tour,dot,e,comp,id,act)
    # query
    q=int(input())
    for _ in range(q):
        Q=list(map(int,input().split()))
        if(Q[0]==1):
            tree.add(tour.begin[Q[1]]+1,tour.end[Q[1]],Q[2])
        else:
            print(tree.sum(0,tour.begin[Q[1]]+1)[0])
resolve()
