# https://atcoder.jp/contests/abc103/tasks/abc103_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    AB=[list(map(int,input().split())) for _ in range(m)]
    AB.sort(lambda x:(x[1],x[0]))
    cnt=0
    L,R=AB[0]
    for a,b in AB:
        L=max(L,a)
        if(L>=R):
            cnt+=1
            L=a
            R=b
    print(cnt+1)
resolve()
