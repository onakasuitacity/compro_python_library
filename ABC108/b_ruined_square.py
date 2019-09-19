# https://atcoder.jp/contests/abc108/tasks/abc108_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    x1,y1,x2,y2=map(int,input().split())
    x,y=x2-x1,y2-y1
    x3,y3=x2-y,y2+x
    x4,y4=x3-x,y3-y
    print(x3,y3,x4,y4)
resolve()
