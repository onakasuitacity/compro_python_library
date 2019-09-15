# https://atcoder.jp/contests/abc141/tasks/abc141_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    s=input()
    if s=="Sunny":
        print("Cloudy")
    elif s=="Cloudy":
        print("Rainy")
    else:
        print("Sunny")

resolve()
