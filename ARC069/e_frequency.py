# https://atcoder.jp/contests/arc069/tasks/arc069_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    AI=[(a,i) for i,a in enumerate(map(int,input().split()))]
    AI.append((0,-1))
    AI.sort(reverse=1)

    m=INF
    ans=[0]*n
    for i in range(n):
        d=AI[i][0]-AI[i+1][0]
        m=min(m,AI[i][1])
        ans[m]+=(i+1)*d

    print(*ans,sep='\n')
resolve()
