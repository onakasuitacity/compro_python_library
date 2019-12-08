# https://atcoder.jp/contests/arc026/tasks/arc026_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    if(n<=5):
        print(b*n)
        return
    ans=5*b
    n-=5
    print(ans+n*a)
resolve()
