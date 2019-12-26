# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    print(b-a+1)
resolve()
