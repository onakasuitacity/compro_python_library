# https://atcoder.jp/contests/abc084/tasks/abc084_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from math import ceil
def resolve():
    n=int(input())
    CSF=[tuple(map(int,input().split())) for _ in range(n-1)]
    for i in range(n-1):
        now=0
        for j in range(i,n-1):
            c,s,f=CSF[j]
            now=f*ceil(max(s,now)/f)+c
        print(now)
    print(0)
resolve()
