# 
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    def dfs(s):
        if int(s)>n: return 0
        res=int(all(s.count(c)>=1 for c in "753"))
        for c in "753":
            res+=dfs(s+c)
        return res
    print(dfs('0'))
resolve()
