# https://atcoder.jp/contests/agc003/tasks/agc003_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[(int(input()),i) for i in range(n)]
    A.sort()
    d=0
    for i,tup in enumerate(A):
        a,j=tup
        d+=abs(j-i)%2

    print(d//2)
resolve()
