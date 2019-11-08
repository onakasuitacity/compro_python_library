# https://atcoder.jp/contests/abc127/tasks/abc127_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    if(a>=13):
        print(b)
    elif(a<=5):
        print(0)
    else:
        print(b//2)
resolve()
