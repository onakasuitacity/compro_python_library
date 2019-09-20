# RollingHash
# https://ei1333.github.io/luzhiled/snippets/string/rolling-hash.html
class RollingHash(object):
    """
    construct: O(N)
    get_hash: O(1)
    LCP: O(logN)
    """
    def __init__(self,S,m1=10**9+9,b1=1007,m2=10**9+7,b2=1009):
        """
        S: string
        m1>m2: prime sufficiently large
        b1,b2: base 0<bi<mi
        """
        assert m1>m2 and 0<b1<m1 and 0<b2<m2
        n=len(S)
        self.__n=n
        self.__m1=m1
        self.__m2=m2
        self.__H1,self.__H2=[0]*(n+1),[0]*(n+1)
        self.__P1,self.__P2=[1]*(n+1),[1]*(n+1)
        for i,s in enumerate(S):
            self.__H1[i+1]=(self.__H1[i]*b1+ord(s))%m1
            self.__H2[i+1]=(self.__H2[i]*b2+ord(s))%m2
            self.__P1[i+1]=self.__P1[i]*b1%m1
            self.__P2[i+1]=self.__P2[i]*b2%m2

    @property
    def len(self):
        return self.__n

    def hash(self,l,r=None):
        """
        l,r: int (0<=l<=r<=n)
        return (hash1,hash2) of S[l:r]
        """
        if r is None: r=self.len
        assert 0<=l<=r<=self.len
        return ((self.__H1[r]-self.__P1[r-l]*self.__H1[l]%self.__m1)%self.__m1,
                (self.__H2[r]-self.__P2[r-l]*self.__H2[l]%self.__m2)%self.__m2)

    def LCP(self,l1,r1=None,rh2=None,l2=0,r2=None):
        if r1 is None: r1=self.len
        if rh2 is None: rh2=self
        if r2 is None: r2=rh2.len
        assert 0<=l1<=r1<=self.len and 0<=l2<=r2<=rh2.len
        L=0
        R=min(r1-l1,r2-l2)
        if self.hash(l1,l1+R)==rh2.hash(l2,l2+R): return R
        while(R-L>1):
            H=(L+R)//2
            if self.hash(l1,l1+H)==rh2.hash(l2,l2+H): L=H
            else: R=H
        return L

#%%
S="abcdefgabchijk"
rh=RollingHash(S)
print(rh.LCP(0,l2=7)) # 3
