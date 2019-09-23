# https://atcoder.jp/contests/abc039/tasks/abc039_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b,c=map(int,input().split())
    print(2*(a*b+b*c+c*a))
resolve()
