# https://atcoder.jp/contests/abc135/tasks/abc135_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import ceil
    K=int(input())
    X,Y=map(int,input().split())
    # defaultは 0 <= Y <= X
    def trans(u,v):
        if(abs(X)<abs(Y)): u,v=v,u
        if(X<0): u=-u
        if(Y<0): v=-v
        return u,v

    x,y=max(abs(X),abs(Y)),min(abs(X),abs(Y))
    if(K%2==0 and (X+Y)&1):
        print(-1)
        return

    # x+y<K
    if(x+y<K and (x+y)&1):
        print(3)
        print(*trans(x,-K+x))
        print(*trans(x+(K+x-y)//2,-(K-x-y)//2))
        print(*trans(x,y))
        return
    if(x+y<K and (not (x+y)&1)):
        print(2)
        print(*trans((x+y)//2,-K+(x+y)//2))
        print(*trans(x,y))
        return

    # x+y=K
    if(x+y==K):
        print(1)
        print(*trans(x,y))
        return
    
    # x+y>K
    c=(-x-y)%K
    n=ceil((x+y)/K)+(c&1)
    l=(K*n-x-y)//2
    print(n)
    nx,ny=K-l,-l
    print(*trans(nx,ny))
    while(nx+K<=x):
        nx+=K
        print(*trans(nx,ny))
    nx,ny=x,ny+(K-(x-nx))
    print(*trans(nx,ny))
    while(ny+K<=y):
        ny+=K
        print(*trans(nx,ny))
resolve()
