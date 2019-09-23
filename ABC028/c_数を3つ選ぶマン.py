# https://atcoder.jp/contests/abc028/tasks/abc028_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import combinations
    A=list(map(int,input().split()))
    B=combinations(A,3)
    C=[x+y+z for x,y,z in B]
    C.sort(reverse=1)
    print(C[2])
resolve()
