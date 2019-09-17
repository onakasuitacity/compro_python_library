# https://atcoder.jp/contests/abc015/tasks/abc015_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n,k=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(n)]
    def dfs(num,xor):
        if num==n-1: return xor==0
        for i in range(k):
            if dfs(num+1,xor^A[num][i]): return True
        return False
    print("Found" if dfs(-1,0) else "Nothing")
resolve()
