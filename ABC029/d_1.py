# https://atcoder.jp/contests/abc029/tasks/abc029_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())+1
    ans=0
    for i in range(10):
        d=10**i
        D=10**(i+1)
        ans+=(n//D)*d
        r=n%D
        ans+=max(0,min(d,r-d))
    print(ans)
resolve()
