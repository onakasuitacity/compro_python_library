# LCA with sparse table (O(NlogN),O(1))
class LCA(object):
    def __init__(self,E,root=0):
        """
        E: adjacency matrix
        """
        n=len(E)
        self.__n=n
        self.__E=E
        self.__depth=[0]*n
        self.__begin=[0]*n
        self.__end=[0]*n
        self.__tour=[0]*(2*n-1)
        self.__i=0; self.__d=0
        self.__dfs(root,-1) # Euler tour
        del self.__i,self.__d
        self.__sparce_table()

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

    def __sparce_table(self):
        N=2*self.__n-1
        logN=max(0,(N-1).bit_length())
        table=[[0]*N for _ in range(logN)]
        table[0]=self.__tour[:]
        from itertools import product
        for i,k in product(range(1,logN),range(N)):
            if(k+(1<<(i-1))>=N):
                table[i][k]=table[i-1][k]
            else:
                table[i][k]=min(table[i-1][k],table[i-1][k+(1<<(i-1))])
        self.__table=table  

    @property
    def depth(self):
        return self.__depth

    def get(self,u,v):
        l=self.__begin[u]; r=self.__begin[v]
        if(l>r): l,r=r,l
        r+=1
        i=max(0,(r-l-1).bit_length()-1)
        return min(self.__table[i][l],self.__table[i][r-(1<<i)])[1]

# example
N=6
V=list(range(N))
E=[{1,2},{0},{0,3,4,5},{2},{2},{2}]

###
#    0
#   / \
#  1   2
#     /|\
#    3 4 5

a=LCA(E,0)
a.get(3,4)
