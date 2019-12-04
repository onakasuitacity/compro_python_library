# https://atcoder.jp/contests/agc038/tasks/agc038_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w,a,b=map(int,input().split())
    s='1'*a+'0'*(w-a)
    t='0'*a+'1'*(w-a)
    for i in range(b):
        print(s)
    for i in range(h-b):
        print(t)
resolve()
