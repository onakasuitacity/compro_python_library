# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    m1,d1=map(int,input().split())
    m2,d2=map(int,input().split())
    print(0 if(d2-d1==1) else 1)
resolve()
