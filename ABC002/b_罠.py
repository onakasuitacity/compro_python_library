# https://atcoder.jp/contests/abc002/tasks/abc002_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    w=input()
    import re
    print(re.sub('[aiueo]','',w))
resolve()
