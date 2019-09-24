# https://atcoder.jp/contests/abc017/tasks/abc017_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    S=input()
    I=["ch",'o','k','u']
    for pattern in I:
        S=S.replace(pattern,'')
    print("YES" if not S else "NO")
resolve()
