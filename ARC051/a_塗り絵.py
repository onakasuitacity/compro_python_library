# https://atcoder.jp/contests/arc051/tasks/arc051_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import product
    x1,y1,r=map(int,input().split())
    x2,y2,x3,y3=map(int,input().split())
    A={(x,y) for x,y in product(range(x1-r,x1+r+1),range(y1-r,y1+r+1)) if (x-x1)**2+(y-y1)**2<=r**2}
    B={(x,y) for x,y in product(range(x2,x3+1),range(y2,y3+1))}
    print("YES" if A-B else "NO")
    print("YES" if B-A else "NO")
resolve()
