# https://atcoder.jp/contests/abc142/tasks/abc142_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    B=[(i,a) for i,a in enumerate(A)]
    B.sort(key=lambda x:x[1])
    for b in B:
        print(b[0]+1,end=' ')
resolve()
