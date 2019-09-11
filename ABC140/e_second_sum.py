# https://atcoder.jp/contests/abc140/tasks/abc140_e
class BIT(object):
    from operator import add
    def __init__(self,A,f=add):
        N=len(A)
        self.__len=N
        self.__f=f
        # built (O(N))
        self.__bit=A[:] # shallow copy
        for i in range(N):
            j=i+((i+1)&-(i+1))
            if j<N: self.tree[j]=self.func(self.tree[i],self.tree[j])

    def __repr__(self):
        return str(self.tree)

    @property
    def func(self):
        return self.__f

    @property
    def tree(self): # getterにしてる意味あんまない
        return self.__bit

    def add(self,i,w):
        while(i<self.__len):
            self.tree[i]=self.func(self.tree[i],w)
            i+=(i+1)&-(i+1)

    def sum(self,i):
        res=0
        while(i>-1):
            res=self.func(res,self.tree[i])
            i-=(i+1)&-(i+1)
        return res

    def bisect_left(self,w):
        # sum(A)より大きければ一番右
        if w>self.sum(self.__len-1): return self.__len
        # 1個しかなく、右じゃないなら左
        elif self.__len==1: return 0
        # それ以外だと、len未満の2のべき乗からスタート
        n=2**((self.__len-1).bit_length()-1)
        res=0
        while(n):
            if res+n-1>self.__len-1: # index over(2べきじゃないときに起こる)
                n//=2
                continue
            if w<=self.tree[res+n-1]: # 左にいく
                n//=2
            else: # 右にいく
                w-=self.tree[res+n-1]
                res+=n
                n//=2
        return res

    def bisect_right(self,w):
        if w>=self.sum(self.__len-1): return self.__len
        elif self.__len==1: return 0
        n=2**((self.__len-1).bit_length()-1)
        res=0
        while(n):
            if w<self.tree[res+n-1]:
                n//=2
            else:
                w-=self.tree[res+n-1]
                res+=n
                n//=2
        return res

# input
n=int(input())
A=list(map(int,input().split()))
# built idx
idx=[0]*n
for i,a in enumerate(A): idx[a-1]=i

# built bit
bit=BIT([0]*n)

# calculate
score=0
for k in range(n,0,-1):
    i=idx[k-1]
    bit.add(i,1)
    s=bit.sum(i)
    # 0.5を引くことでbisect_left=bisect_right
    l0=bit.bisect_left(s-1.5)-(s<=1) # 一番左を含むか含まないかで場合分け
    l1=bit.bisect_left(s-2.5)-(s<=2) # 一番左を含むか含まないかで場合分け
    r0=bit.bisect_left(s+0.5)
    r1=bit.bisect_left(s+1.5)
    score+=k*((l0-l1)*(r0-i)+(r1-r0)*(i-l0))
print(score)
