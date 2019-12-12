# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    x=0
    while((x+1)**2<=n): x+=1
    print(x)
resolve()
