# https://atcoder.jp/contests/abc041/tasks/abc041_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=map(int,input().split())
    A=[(i,a) for i,a in enumerate(A)]
    from operator import itemgetter
    A.sort(key=itemgetter(1),reverse=1)
    for i,a in A:
        print(i+1)
resolve()
