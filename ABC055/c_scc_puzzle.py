# https://atcoder.jp/contests/abc055/tasks/arc069_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    if(m-2*n<=0):
        print(m//2)
        return

    ans=n
    m=m-2*n
    print(ans+m//4)
resolve()
