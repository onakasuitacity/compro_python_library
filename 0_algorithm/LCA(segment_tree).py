class LCA(object):
    def __init__(self,E,root=0):
        """
        E: adjacency matrix
        """
        n=len(E)
        self.__E=E
        self.__depth=[0]*n
        self.__begin=[0]*n
        self.__end=[0]*n
        self.__tour=[0]*(2*n-1)
        self.__i=0; self.__d=0
        self.__dfs(root,-1) # Euler tour
        del self.__i,self.__d
        self.__tree=SegmentTree(self.__tour,min,(float("inf"),float("inf")))

    def __dfs(self,v,p):
        self.__begin[v]=self.__i
        self.__depth[v]=self.__d
        self.__tour[self.__i]=(self.__d,v)
        self.__i+=1
        for u in self.__E[v]:
            if(u==p): continue
            self.__d+=1
            self.__dfs(u,v)
            self.__d-=1
            self.__tour[self.__i]=(self.__d,v)
            self.__i+=1
        self.__end[v]=self.__i

    @property
    def depth(self):
        return self.__depth

    def get(self,u,v):
        i=self.__begin[u]; j=self.__begin[v]
        if(i>j): i,j=j,i
        return self.__tree.sum(i,j+1)[1]

class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n)
        for i in range(len(A)):
            self.__node[i+n]=A[i]
        for i in range(n-1,-0,-1):
            self.__node[i]=dot(self.__node[2*i],self.__node[2*i+1])

    def sum(self,l,r):
        vl,vr=self.__e,self.__e
        l+=self.__n; r+=self.__n
        while(l<r):
            if(l%2==1):
                vl=self.__dot(vl,self.__node[l])
                l+=1
            l//=2
            if(r%2==1):
                r-=1
                vr=self.__dot(self.__node[r],vr)
            r//=2
        return self.__dot(vl,vr)
