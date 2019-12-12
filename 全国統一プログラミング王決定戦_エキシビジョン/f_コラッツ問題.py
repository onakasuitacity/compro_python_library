# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=1000
    x=1789997546303
    ans=[1]*1001
    while(n):
        ans[n]=x
        x=3*x+1 if(x&1) else x//2
        n-=1
    print(ans[int(input())])
resolve()
