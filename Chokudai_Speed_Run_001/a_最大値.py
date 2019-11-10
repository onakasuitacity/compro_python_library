# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    int(input())
    print(max(map(int,input().split())))
resolve()
