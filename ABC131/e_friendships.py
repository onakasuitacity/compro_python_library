# 
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    s=(n-1)*(n-2)//2-k
    if(s<0):
        print(-1)
        return
    print(s+n-1)
    from itertools import product
    E=[(u,v) for u,v in product(range(2,n+1),repeat=2) if u<v]
    for i in range(n-1):
        print(1,i+2) # 1-rooted
    for i in range(s):
        print(*E[i])
resolve()
