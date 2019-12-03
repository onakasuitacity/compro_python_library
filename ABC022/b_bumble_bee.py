# https://atcoder.jp/contests/abc022/tasks/abc022_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    C=[0]*(100001)
    ans=0
    for _ in range(n):
        a=int(input())
        ans+=(C[a]>0)
        C[a]+=1
    print(ans)
resolve()
