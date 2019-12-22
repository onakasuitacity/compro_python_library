# https://atcoder.jp/contests/arc040/tasks/arc040_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    G=[s for _ in range(n) for s in input()]
    r=G.count('R')
    b=G.count('B')

    if(r>b):
        print("TAKAHASHI")
    elif(r<b):
        print("AOKI")
    else:
        print("DRAW")
resolve()
