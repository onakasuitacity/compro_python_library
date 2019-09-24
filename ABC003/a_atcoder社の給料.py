# https://atcoder.jp/contests/abc003/tasks/abc003_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    print(10000*(n+1)//2)
resolve()
