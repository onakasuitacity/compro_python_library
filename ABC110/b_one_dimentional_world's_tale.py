# https://atcoder.jp/contests/abc110/tasks/abc110_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m,x,y=map(int,input().split())
    max_x=max(map(int,input().split()))
    min_y=min(map(int,input().split()))
    print("No War" if x<min_y<=y and max_x<min_y else "War")
resolve()
