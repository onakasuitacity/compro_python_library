# https://atcoder.jp/contests/kupc2019/tasks/kupc2019_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    m,k=map(int,input().split())
    a=0
    ans=0
    while(m>a):
        ans+=1
        a=(2*k+1)*a+k
    print(ans)
resolve()
