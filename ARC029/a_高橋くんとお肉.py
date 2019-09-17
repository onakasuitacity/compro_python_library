# https://atcoder.jp/contests/arc029/tasks/arc029_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    T=[int(input()) for _ in range(n)]
    ans=INF
    for k in range(1<<n):
        a=b=0
        for i in range(n):
            if k&(1<<i): a+=T[i]
            else: b+=T[i]
        ans=min(ans,max(a,b))
    print(ans)

resolve()
