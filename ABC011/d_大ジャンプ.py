# https://atcoder.jp/contests/abc011/tasks/abc011_4
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,d=map(int,input().split())
    x,y=map(int,input().split())
    if x%d or y%d:
        print(0)
        return
    x//=d; y//=d
    x=abs(x); y=abs(y)
    if x+y>n or (x+y+n)%2:
        print(0)
        return
    from math import factorial
    ans=0
    k=(n-x-y)//2
    for i in range(k+1):
        ans+=factorial(n)//factorial(x+i)//factorial(i)//factorial(y+k-i)//factorial(k-i)
    print(ans/4**n)
resolve()
