# https://atcoder.jp/contests/arc017/tasks/arc017_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    now=-INF
    cnt=0
    ans=0
    for _ in range(n):
        a=int(input())
        if(a>now): cnt+=1
        else: cnt=1
        now=a
        ans+=(cnt>=k)

    print(ans)
resolve()
