# https://atcoder.jp/contests/pakencamp-2019-day4/tasks/pakencamp_2019_day4_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    R=list(range(n))
    for i in range(n-1,-1,-1):
        d=n-R[i] # 増やせる数
        R[i]+=min(d,x)
        x-=min(d,x)

    k=10000
    A=[None]*n
    for i in range(n):
        if(R[i]==i):
            A[i]=k+1
        elif(R[i]==n):
            A[i]=1
        else:
            A[i]=k-(R[i]-i)+1

    print(k)
    print(*A)
resolve()
