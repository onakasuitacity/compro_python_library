# https://atcoder.jp/contests/abc059/tasks/arc072_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x,y=map(int,input().split())
    print("Alice" if(abs(x-y)>1) else "Brown")
resolve()
