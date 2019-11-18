# https://atcoder.jp/contests/abc095/tasks/arc096_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c,x,y=map(int,input().split())
    ans=0

    # 常に x>=y としておく
    if(x<y):
        x,y=y,x
        a,b=b,a

    # はじめに a+b と 2c の大小で y を埋める
    if(a+b>=2*c):
        ans+=y*2*c
        x-=y
    else:
        ans+=y*b

    # 次に残った x を、a と 2c の大小で埋める
    if(a>=2*c):
        ans+=x*2*c
    else:
        ans+=x*a

    print(ans)
resolve()
