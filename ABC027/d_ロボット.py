# https://atcoder.jp/contests/abc027/tasks/abc027_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    C=[None]*n
    for i in range(n):
        if(S[i]=='M'): C[i]=0
        elif(S[i]=='+'): C[i]=1
        else: C[i]=-1
    for i in range(n-1,0,-1):
        C[i-1]+=C[i]

    X=[]
    for i,s in enumerate(S):
        if(s=='M'): X.append(C[i])
    X.sort()
    m=len(X)//2
    print(-1*sum(X[:m])+sum(X[m:]))
resolve()
