# https://atcoder.jp/contests/abc083/tasks/arc088_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x,y=map(int,input().split())
    ans=0
    while(y>=x):
        ans+=1
        x*=2
    print(ans)
resolve()
