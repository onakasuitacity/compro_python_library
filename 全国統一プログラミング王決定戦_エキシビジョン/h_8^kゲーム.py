# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_h
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    n%=9
    print("Win" if(n in [1,3,5,7,8]) else "Lose") # 0 1 0 1 0 1 0 1 1
resolve()
