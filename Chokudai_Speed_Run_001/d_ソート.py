# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    int(input())
    A=list(map(int,input().split()))
    A.sort()
    print(*A)
resolve()
