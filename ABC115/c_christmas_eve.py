# https://atcoder.jp/contests/abc115/submissions/7981801
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.buffer.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    H=[int(input()) for _ in range(n)]
    H.sort()
    ans=INF
    for i in range(n-k+1):
        ans=min(ans,H[i+k-1]-H[i])
    print(ans)
resolve()
