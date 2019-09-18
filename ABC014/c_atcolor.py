# https://atcoder.jp/contests/abc014/tasks/abc014_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    N_MAX=10**6+1
    n=int(input())
    imos=[0]*(N_MAX+1)
    for _ in range(n):
        a,b=map(int,input().split())
        imos[a]+=1
        imos[b+1]-=1
    imos.pop()
    for i in range(N_MAX-1):
        imos[i+1]+=imos[i]
    print(max(imos))
resolve()
