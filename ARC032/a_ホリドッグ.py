# https://atcoder.jp/contests/arc032/tasks/arc032_1
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    print("WANWAN" if int(input())==2 else "BOWWOW")
resolve()
