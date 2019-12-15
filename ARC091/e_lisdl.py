# https://atcoder.jp/contests/arc091/tasks/arc091_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,a,b=map(int,input().split())
    if(a+b>n+1):
        print(-1)
        return
    if(a*b<n):
        print(-1)
        return

    ans=list(range(b,0,-1))
    now=b
    d=a*b-n
    for _ in range(a-1):
        k=min(d,b-1)
        d-=k
        next=now+(b-k)
        for i in range(next,now,-1):
            ans.append(i)
        now=next

    print(*ans)
resolve()
