# https://atcoder.jp/contests/abc112/tasks/abc112_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    X,Y,H=[0]*n,[0]*n,[0]*n
    for i in range(n):
        X[i],Y[i],H[i]=map(int,input().split())

    def check(x0,y0):
        # H[i]が0でない値に対して、x0,y0から高さをfixする
        for i in range(n):
            if(H[i]==0): continue
            h=H[i]+abs(X[i]-x0)+abs(Y[i]-y0)
            break
        # この h に対して、残りが整合しているかcheck
        for i in range(n):
            if(H[i]!=max(0,h-abs(X[i]-x0)-abs(Y[i]-y0))):
                return False
        return x0,y0,h

    from itertools import product
    for x0,y0 in product(range(101),repeat=2):
        A=check(x0,y0)
        if(A):
            print(*A)
            return
resolve()
