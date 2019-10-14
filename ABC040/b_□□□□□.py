# https://atcoder.jp/contests/abc040/tasks/abc040_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.buffer.readline().rstrip()
def resolve():
    n=int(input())
    d=n-int(n**.5)**2
    ans=d
    for i in range(1,n+1):
        for j in range(d):
            if(n>=i*(i+j)):
                ans=min(ans,j+n-i*(i+j))
    print(ans)
resolve()
