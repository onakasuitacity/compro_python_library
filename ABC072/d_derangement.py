# https://atcoder.jp/contests/abc072/tasks/arc082_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    P=list(map(lambda x:int(x)-1,input().split()))
    cnt=0
    for i in range(n-1):
        if(P[i]==i and P[i+1]==i+1):
            cnt+=1
            P[i],P[i+1]=P[i+1],P[i]
    print(cnt+sum(P[i]==i for i in range(n)))
resolve()
