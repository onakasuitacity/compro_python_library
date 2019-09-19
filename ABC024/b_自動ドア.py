# https://atcoder.jp/contests/abc024/tasks/abc024_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,t=map(int,input().split())
    T=[int(input()) for _ in range(n)]
    ans=t # 最初は押された状態にしておく
    for i in range(n-1):
        ans+=min(t,T[i+1]-T[i])
    print(ans)
resolve()
