# https://atcoder.jp/contests/abc007/tasks/abc007_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    A=input()
    print(-1 if A=='a' else 'a')
resolve()
