# https://atcoder.jp/contests/abc147/tasks/abc147_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    a=sum(map(int,input().split()))
    print("bust" if(a>=22) else "win")
resolve()
