# https://atcoder.jp/contests/abc146/tasks/abc146_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    S=list(input())
    S=list(map(int,S))[::-1]
    ans=[]
    now=0
    while(now<n):
        next=now
        for i in range(1,m+1):
            if(now+i==n):
                next=n
                break
            if(S[now+i]==0): next=now+i
        if(now==next):
            print(-1)
            return
        ans.append(next-now)
        now=next
    ans=ans[::-1]
    print(*ans)
resolve()
