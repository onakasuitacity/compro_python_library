# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    S=input()
    n=len(S)
    print(*range(1,n+1),sep='\n')
resolve()
