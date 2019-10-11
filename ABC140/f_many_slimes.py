# https://atcoder.jp/contests/abc140/tasks/abc140_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    N=1<<n
    s=list(map(int,input().split()))
    s.sort(reverse=1)
    p=[s[0]]
    s[0]=INF
    for _ in range(n):
        p.sort(reverse=1)
        q=p[:]
        idx=0
        for i in q:
            while(idx!=N):
                j=s[idx]
                idx+=1
                if(i<=j): continue
                p.append(j)
                s[idx-1]=INF
                break
    print("Yes" if len(p)==N else "No")
resolve()
