# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    print(a*b*b)
resolve()
