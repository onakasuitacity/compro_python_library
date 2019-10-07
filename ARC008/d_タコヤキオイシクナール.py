# https://atcoder.jp/contests/arc008/tasks/arc008_4
class SegmentTree(object):
    def __init__(self,A,dot,e):
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__node=[e]*(2*n-1)
        for i in range(len(A)):
            self.__node[n+i-1]=A[i]
        for i in range(n-2,-1,-1):
            self.__node[i]=dot(self.__node[2*i+1],self.__node[2*i+2])

    def update(self,i,c):
        i+=self.__n-1
        node=self.__node
        node[i]=c
        while(i!=0):
            i=(i-1)//2
            node[i]=self.__dot(node[2*i+1],node[2*i+2])

    def __get_range(self,l,r):
        if l>=r: return [],[]
        Left,Right=[],[]
        n=self.__n
        l+=n-1; r+=n-2
        while(l<r):
            if l%2==0:
                Left.append(l)
            if r%2==1:
                Right.append(r)
                r-=1
            l=l//2; r=(r-1)//2
        if l==r:
            if l%2==0: Left.append(l)
            else: Right.append(l)
        return Left,Right

    def sum(self,l,r):
        Left,Right=self.__get_range(l,r)
        res=self.__e
        for i in Left+Right[::-1]:
            res=self.__dot(res,self.__node[i])
        return res

import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    e=(1,0)
    dot=lambda a,b:(a[0]*b[0],a[1]*b[0]+b[1])
    Point=set()
    Query=[]
    for _ in range(m):
        p,a,b=input().split()
        p=int(p)-1
        a,b=float(a),float(b)
        Point.add(p)
        Query.append((p,a,b))
    Point=sorted(Point)
    n=len(Point)
    id={Point[i]:i for i in range(n)}
    # segment tree
    A=[e]*n # coordinate compression
    tree=SegmentTree(A,dot,e)
    res=[1]
    for p,a,b in Query:
        tree.update(id[p],(a,b))
        res.append(sum(tree.sum(0,n)))
    print(min(res))
    print(max(res))
resolve()
