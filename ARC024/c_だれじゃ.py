# https://atcoder.jp/contests/arc024/tasks/arc024_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
class ZobristHash(object):
    __mod1=10**9+7; __mod2=10**9+9

    def __init__(self,s):
        n=len(s)
        self.__s=s
        self.__n=len(s)
        m1=self.__mod1; m2=self.__mod2
        H1,H2=[1]*(n+1),[1]*(n+1)
        for i in range(n):
            H1[i+1]=ord(s[i])*H1[i]%m1
            H2[i+1]=ord(s[i])*H2[i]%m2
        self.__H1=H1; self.__H2=H2

    def hash(self,l,r):
        m1=self.__mod1; m2=self.__mod2
        H1=self.__H1; H2=self.__H2
        return (H1[r]*pow(H1[l],m1-2,m1)%m1,H2[r]*pow(H2[l],m2-2,m2)%m2)

def resolve():
    from collections import defaultdict
    n,k=map(int,input().split())
    z=ZobristHash(input())
    d=defaultdict(lambda :-INF)
    for i in range(n-k+1):
        hash=z.hash(i,i+k)
        j=d[hash]
        if j==-INF:
            d[hash]=i
        else:
            if i-j>=k:
                print("YES")
                return
    print("NO")
resolve()
