# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x,y,z=map(int,input().split())
    ans=0
    for _ in range(n):
        a,b=map(int,input().split())
        ans+=(x<=a and y<=b and z<=(a+b))
    print(ans)
resolve()
