# https://atcoder.jp/contests/abc128/tasks/abc128_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    S=list(map(int,input().split()))
    ans=0
    for d in range(1,n):
        score=0
        P=set()
        for x in range(n//d):
            a=(n-1)-x*d
            if(a<=d): break
            if((x*d in P) or (n-1-x*d in P)): break
            if(x*d==n-1-x*d): break
            score+=S[x*d]
            score+=S[n-1-x*d]
            P.add(x*d)
            P.add(n-1-x*d)
            ans=max(ans,score)
    print(ans)
resolve()
