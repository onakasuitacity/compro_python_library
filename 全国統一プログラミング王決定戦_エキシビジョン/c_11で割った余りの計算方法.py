# https://atcoder.jp/contests/nikkei2019-ex/tasks/nikkei2019ex_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    print(int(input())%11)
resolve()
