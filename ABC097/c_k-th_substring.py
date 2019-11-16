# https://atcoder.jp/contests/abc097/tasks/arc097_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

class SuffixArray(object):
    def __init__(self,s):
        self.__s=s
        self.__n=len(s)
        self.__suffix_array()
        self.__lcp_array()
        self.__sparse_table()

    def __suffix_array(self):
        s=self.__s; n=self.__n
        sa=list(range(n))
        rank=[ord(s[i]) for i in range(n)]
        tmp=[0]*n
        k=1
        cmp_key=lambda i:(rank[i],rank[i+k] if i+k<n else -1)
        while(k<=n):
            sa.sort(key=cmp_key)
            tmp[sa[0]]=0
            for i in range(1,n):
                tmp[sa[i]]=tmp[sa[i-1]]+(cmp_key(sa[i-1])<cmp_key(sa[i]))
            rank=tmp[:]
            k<<=1
        self.__sa=sa
        self.__rank=rank

    def __lcp_array(self):
        s=self.__s; n=self.__n
        sa=self.__sa; rank=self.__rank
        lcp=[0]*n
        h=0
        for i in range(n):
            j=sa[rank[i]-1]
            if(h>0): h-=1
            if(rank[i]==0): continue
            while(j+h<n and i+h<n and s[j+h]==s[i+h]): h+=1
            lcp[rank[i]]=h
        self.__lcp=lcp

    def __sparse_table(self):
        n=self.__n
        logn=max(1,(n-1).bit_length())
        table=[[0]*n for _ in range(logn)]
        table[0]=self.__lcp[:]
        from itertools import product
        for i,k in product(range(1,logn),range(n)):
            if(k+(1<<(i-1))>=n): table[i][k]=table[i-1][k]
            else: table[i][k]=min(table[i-1][k],table[i-1][k+(1<<(i-1))])
        self.__table=table

    @property
    def suffix(self):
        return self.__sa

    def lcp(self,a,b):
        if(a==b): return self.__n-a
        l,r=self.__rank[a],self.__rank[b]
        l,r=min(l,r)+1,max(l,r)+1
        i=max(0,(r-l-1).bit_length()-1)
        table=self.__table
        return min(table[i][l],table[i][r-(1<<i)])

def resolve():
    S=input()
    n=len(S)
    k=int(input())

    sa=SuffixArray(S)
    D=set()
    for i in sa.suffix:
        for j in range(i+1,n+1):
            D.add(S[i:j])
            if(len(D)==k):
                print(sorted(D)[-1])
                return
resolve()
