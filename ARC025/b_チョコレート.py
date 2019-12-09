# https://atcoder.jp/contests/arc025/tasks/arc025_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()

class cumsum2d(object):
    def __init__(self,m,n):
        self.__m=m
        self.__n=n
        self.__S=[[0]*(n+1) for _ in range(m+1)]

    def __repr__(self):
        return '\n'.join(' '.join(map(str,s)) for s in self.__S)

    def add(self,i,j,w):
        self.__S[i+1][j+1]+=w

    def cumulate(self):
        S=self.__S
        for i in range(self.__m):
            for j in range(self.__n):
                S[i+1][j+1]+=S[i+1][j]+S[i][j+1]-S[i][j]

    def sum(self,i0,j0,i1,j1):
        S=self.__S
        return S[i1][j1]-S[i0][j1]-S[i1][j0]+S[i0][j0]

def resolve():
    h,w=map(int,input().split())
    C=cumsum2d(h,w)
    for i in range(h):
        for j,x in enumerate(map(int,input().split())):
            if((i+j)&1): C.add(i,j,-x)
            else: C.add(i,j,x)
    C.cumulate()
    
    ans=0
    from itertools import product
    for i0,j0 in product(range(h),range(w)):
        for i1,j1 in product(range(i0+1,h+1),range(j0+1,w+1)):
            if(C.sum(i0,j0,i1,j1)==0):
                ans=max(ans,(i1-i0)*(j1-j0))
    print(ans)
resolve()
