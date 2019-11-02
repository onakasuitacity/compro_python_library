# https://atcoder.jp/contests/abc136/tasks/abc136_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]

def resolve():
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    D=divisors(sum(A))
    def check(d):
        P=[]
        N=[]
        for i in range(n):
            r=A[i]%d
            if(not r): continue
            P.append(d-r)
        P.sort()
        l=len(P)
        N=[d-p for p in P]
        N.reverse()
        PS=[0]*(l+1)
        NS=[0]*(l+1)
        for i in range(l):
            PS[i+1]=PS[i]+P[i]
            NS[i+1]=NS[i]+N[i]
        NS.reverse()
        res=INF
        for i in range(l):
            res=min(res,max(PS[i],NS[i+1]))
        return res<=k
    ans=1
    for d in D:
        if(check(d)): ans=d
    print(ans)
resolve()
