# https://atcoder.jp/contests/abc090/tasks/arc091_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    if(k==0):
        print(n**2)
        return
    ans=0
    for b in range(k+1,n+1):
        q=(n-k)//b+1
        ans+=q*(b-k)-max(0,(q*b-1)-n)
    print(ans)
resolve()
