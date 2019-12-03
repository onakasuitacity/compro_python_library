# https://atcoder.jp/contests/abc005/tasks/abc005_4
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

    def sum(self,i0,i1,j0,j1):
        S=self.__S
        return S[i1][j1]-S[i0][j1]-S[i1][j0]+S[i0][j0]

def resolve():
    n=int(input())
    C=cumsum2d(n,n)
    for i in range(n):
        for j,d in enumerate(map(int,input().split())):
            C.add(i,j,d)
    C.cumulate()

    score=[-INF]*(n**2+1)
    from itertools import product
    for di,dj in product(range(1,n+1),repeat=2):
        for i,j in product(range(n-di+1),range(n-dj+1)):
            score[di*dj]=max(score[di*dj],C.sum(i,i+di,j,j+dj))
    for i in range(n**2):
        score[i+1]=max(score[i+1],score[i])

    for _ in range(int(input())):
        print(score[int(input())])
resolve()
