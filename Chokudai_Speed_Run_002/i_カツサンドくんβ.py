# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_i
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from math import ceil
def cmp(X,Y):
    s=ceil(X[0]/Y[1])
    t=ceil(Y[0]/X[1])
    return s<t

def resolve():
    n=int(input())
    a,b=map(int,input().split())
    ABI=[0]*n
    X=(a,b,1)
    ABI[0]=X
    for i in range(n-1):
        a,b=map(int,input().split())
        Y=(a,b,i+2)
        ABI[i+1]=Y
        if(cmp(X,Y)):
            X=Y
    ABI.remove(X)
    print(X[2] if(all(cmp(ABI[i],X) for i in range(n-1))) else -1)
resolve()
