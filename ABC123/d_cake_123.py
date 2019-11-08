# https://atcoder.jp/contests/abc123/tasks/abc123_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x,y,z,k=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    S=[]
    T=[]
    from itertools import product
    for a,b in product(A,B):
        S.append(a+b)
    S.sort(reverse=1)
    S=S[:k]
    for s,c in product(S,C):
        T.append(s+c)
    T.sort(reverse=1)
    for i in range(k):
        print(T[i])
resolve()
