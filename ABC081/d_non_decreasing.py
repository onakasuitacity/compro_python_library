# https://atcoder.jp/contests/abc081/tasks/arc086_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    m=min(A); M=max(A)
    mi=A.index(m)+1; Mi=A.index(M)+1
    print(2*n-2)
    # 全て非負にする
    if(-m<=M):
        for i in range(1,n+1):
            if(i==Mi): continue
            print(Mi,i)
        for i in range(1,n):
            print(i,i+1)
    # 全て非正にする
    else:
        for i in range(1,n+1):
            if(i==mi): continue
            print(mi,i)
        for i in range(n,1,-1):
            print(i,i-1)
resolve()
