# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    if(2*k>n+1):
        print(-1)
        return
    
    h=(2*k+3*n-1)//2
    for i in range((n+1)//2):
        print(k+2*i,h-i,k+2*n+i)
    for i in range(n//2):
        print(k+1+i*2,k+2*n-1-i,k+2*n+((n-1)//2)+i+1)
resolve()
