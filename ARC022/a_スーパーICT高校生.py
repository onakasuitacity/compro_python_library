# https://atcoder.jp/contests/arc022/tasks/arc022_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    import re
    pattern="^.*?[iI].*?[cC].*?[tT].*$"
    print("YES" if re.match(pattern,input()) else "NO")
resolve()
