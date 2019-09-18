# https://atcoder.jp/contests/abc017/tasks/abc017_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    imos=[0]*(m+1)
    total=0
    for _ in range(n):
        l,r,s=map(int,input().split())
        total+=s
        imos[l-1]+=s
        imos[r]-=s
    for i in range(m):
        imos[i+1]+=imos[i]
    imos.pop()
    print(total-min(imos))
resolve()
